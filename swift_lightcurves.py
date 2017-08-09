import os.path
import matplotlib.pyplot as plt

# generating list of ascii files
SWIFT_ascii_files=[]
for file in os.listdir("ascii_files"):
    if file.endswith(".txt"):
        SWIFT_ascii_files.append(file)

# extracting data from ascii files
for i in range(len(SWIFT_ascii_files)):

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

	with open("ascii_files/"+SWIFT_ascii_files[i]) as f:
	    for line in f: #Line is a string
	        numbers_str = line.split() #split the string on whitespace, return a list of numbers (as strings)
	        numbers_float = [float(x) for x in numbers_str] #convert numbers to floats
	        time.append(numbers_float[0])
	        ch1.append(numbers_float[1])
	        ch1_unc.append(numbers_float[2])
	        ch2.append(numbers_float[3])
	        ch2_unc.append(numbers_float[4])
	        ch3.append(numbers_float[5])
	        ch3_unc.append(numbers_float[6])
	        ch4.append(numbers_float[7])
	        ch4_unc.append(numbers_float[8])
	        ch1234.append(numbers_float[9])
	        ch1234_unc.append(numbers_float[10])
	
	# setting GRB_number for plotting
	GRB_number=str(SWIFT_ascii_files[i])
	GRB_number=GRB_number.replace('_ascii.txt','')

	# plotting and saving lightcurves
	plt.errorbar(time,ch1234,yerr=ch1234_unc) # plt.plot(time,ch1234) #can change it if you dont want error bars
	plt.title('SWIFT '+GRB_number+' ch1+2+3+4')
	plt.xlabel('time (s)')
	plt.ylabel('ch1+2+3+4 (counts/s)')
	GRB_lightcurve=plt.gcf()
	plt.show()
	GRB_lightcurve.savefig('lightcurves/'+GRB_number+'_ch1+2+3+4_lightcurve.jpeg')