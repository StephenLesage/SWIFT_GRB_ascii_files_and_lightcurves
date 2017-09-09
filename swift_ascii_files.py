from astropy.io import fits
import os.path
import numpy as np
import math
import matplotlib.pyplot as plt

# collecting all fits files in the "SWIFT_fits_files" folder
SWIFTfiles=[]
for file in os.listdir("fits_files"):
    if file.endswith(".lc"):
        SWIFTfiles.append(file)

# loop through all SWIFT_fits_files
for x in range(len(SWIFTfiles)):

	# itterating through one fits file at a time
	lc_fits = fits.open('fits_files/'+SWIFTfiles[x])
	# lc_fits.info()	

	# gathering data from fits files
	lc_fits_data = lc_fits[1].data

	# creating empty arrays
	time=[]
	ch1=[]
	ch2=[]
	ch3=[]
	ch4=[]
	ch1234=[]
	ch1_unc=[]
	ch2_unc=[]
	ch3_unc=[]
	ch4_unc=[]
	ch1234_unc=[]	

	# NOTE:
	# ch1 = 15-25 keV
	# ch2 = 25-50 keV
	# ch3 = 50-100 keV
	# ch4 = 100-350 keV
	# ch1+2+3+4 = 15-350 keV	

	# extracting necessary lightcurve data and organizing it into corresponding arrays
	for i in range(len(lc_fits_data)):
		time.append(lc_fits_data[i][0])
		ch1.append(lc_fits_data[i][1][0])
		ch2.append(lc_fits_data[i][1][1])
		ch3.append(lc_fits_data[i][1][2])
		ch4.append(lc_fits_data[i][1][3])
		ch1234.append(lc_fits_data[i][1][0]+lc_fits_data[i][1][1]+lc_fits_data[i][1][2]+lc_fits_data[i][1][3])
		ch1_unc.append(lc_fits_data[i][2][0])
		ch2_unc.append(lc_fits_data[i][2][1])
		ch3_unc.append(lc_fits_data[i][2][2])
		ch4_unc.append(lc_fits_data[i][2][3])
		ch1234_unc.append(math.sqrt((((lc_fits_data[i][2][0])**2)+((lc_fits_data[i][2][1])**2)+((lc_fits_data[i][2][2])**2)+((lc_fits_data[i][2][3])**2))))	

	# getting GRB number and trigger time for plots based on fits file title
	# strip fits file name down to the trigger id
	SWIFTfiles[x]=SWIFTfiles[x].replace('b_4chan_64ms.lc','')
	SWIFTfiles[x]=SWIFTfiles[x].replace('sw','')
	# open text file of grb names and trigger ids
	GRB_number=''
	# compare stripped fits file name to names in tet file to find corresponding grb name
	with open("swift_grbtrigger_and_burstid.txt") as f:
		    for line in f: #Line is a string
		        numbers_str = line.split() #split the string on whitespace, return a list of numbers (as strings)
		        numbers_str[1].strip()
		        if numbers_str[1] == SWIFTfiles[x]:
		        	GRB_number = numbers_str[0]
		        	trigger_time = float(numbers_str[2].strip())

	# adjusting time from "trigger time in BAT MET" to "time since trigger"
	time_since_trigger=[]
	for element in time:
		time_val=element-trigger_time
		time_since_trigger.append(time_val)

	# stacking lightcurve data arrays and turning them into columns
	data=np.array([time_since_trigger,ch1,ch1_unc,ch2,ch2_unc,ch3,ch3_unc,ch4,ch4_unc,ch1234,ch1234_unc])
	data=data.T	

	# saving the data as a ascii text file
	np.savetxt('ascii_files/'+GRB_number+"_ascii.txt",data)	

	# displays lightcurves if desired
	plt.errorbar(time_since_trigger,ch1234,yerr=ch1234_unc) # plt.plot(time,ch1234) #can change it if you dont want error bars
	plt.title('SWIFT '+GRB_number+' ch1+2+3+4')
	plt.xlabel('time (s)')
	plt.ylabel('ch1+2+3+4 (counts/s)')
	GRB_lightcurve=plt.gcf()
	plt.show()
	# saves ightcurves if desired
	GRB_lightcurve.savefig('lightcurves/'+GRB_number+'_ch1+2+3+4_lightcurve.jpeg')