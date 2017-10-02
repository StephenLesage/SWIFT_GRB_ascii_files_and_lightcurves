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

    # compare GRB name to names in burst duration table file to find corresponding t_100 start and stop times
	with open("burst_duration_table.txt") as g:
		    for line in g: #line is a string
		        numbers_str = line.split() #split the string on whitespace, return a list of numbers (as strings)
		        numbers_str[0].strip()
		        if numbers_str[0] == GRB_number:
		        	t_100_start = float(numbers_str[3].strip())
		        	t_100_stop = float(numbers_str[4].strip())
		        	if t_100_start == 0.0 and t_100_stop == 0.0:
		        		t_100_start = time[0]
		        		t_100_stop = time[-1]

    #finding 10% so the plot can show 140% of the burst
 	twenty_percent = (t_100_stop-t_100_start)/10.0

    #find where elements of time array are greater than t_100_start minus 20% and less than the t_100_stop time plus 20%
	beginning_section = [i for i,v in enumerate(time) if v >= t_100_start-twenty_percent]
	adjusted_time = [j for j,v in enumerate(time) if v <= t_100_stop+ twenty_percent]
	
    #getting the indices for t_100_start minus 20% and t_100_stop plus 20%
	first_element_index = beginning_section[0]
	last_element_index = adjusted_time[-1]

	#creating adjusted time and channel arrays
	adj_time = time[first_element_index:last_element_index+1]
	adj_ch1 = ch1[first_element_index:last_element_index+1]
	adj_ch1_unc = ch1_unc[first_element_index:last_element_index+1]
	adj_ch2 = ch2[first_element_index:last_element_index+1]
	adj_ch2_unc = ch2_unc[first_element_index:last_element_index+1]
	adj_ch3 = ch3[first_element_index:last_element_index+1]
	adj_ch3_unc = ch3_unc[first_element_index:last_element_index+1]
	adj_ch4 = ch4[first_element_index:last_element_index+1]
	adj_ch4_unc = ch4_unc[first_element_index:last_element_index+1]
	adj_ch1234 = ch1234[first_element_index:last_element_index+1]
	adj_ch1234_unc = ch1234_unc[first_element_index:last_element_index+1]

	# # plotting and saving the burst lightcurves
	# plt.errorbar(adj_time,adj_ch1234,yerr=adj_ch1234_unc) # plt.plot(adj_time,adj_ch1234) #can change it if you dont want error bars
	# plt.title('SWIFT '+GRB_number+' ch1+2+3+4')
	# plt.xlabel('time (s)')
	# plt.ylabel('ch1+2+3+4 (counts/s)')
	# GRB_lightcurve=plt.gcf()
	# # plt.show()
	# GRB_lightcurve.savefig('burst_lightcurves/'+GRB_number+'_ch1+2+3+4_lightcurve.jpeg')
	# plt.clf()
	# print GRB_number


	# plotting and saving the entire lightcurves
	plt.errorbar(time,ch1234,yerr=ch1234_unc) # plt.plot(time,ch1234) #can change it if you dont want error bars
	plt.title('SWIFT '+GRB_number+' ch1+2+3+4')
	plt.xlabel('time (s)')
	plt.ylabel('ch1+2+3+4 (counts/s)')
	GRB_lightcurve=plt.gcf()
	# plt.show()
	GRB_lightcurve.savefig('lightcurves/'+GRB_number+'_ch1+2+3+4_lightcurve.jpeg')
	plt.clf()
	print GRB_number
