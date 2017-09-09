import urllib

# reading through list of list of grb triggers to loop through them in the url later
with open("swift_grbtrigger_and_burstid.txt") as f:
	for line in f: #line is a string
		numbers_str = line.split() #split the string on whitespace, return a list of numbers (as strings)
		grb_name=numbers_str[0].strip()
		trigger_id=numbers_str[1].strip()

		# saving url name
		url = 'https://swift.gsfc.nasa.gov/results/batgrbcat/'+grb_name+'/data_product/'+trigger_id+'-results/lc/sw'+trigger_id+'b_4chan_64ms.lc'
		
		# web navigation to url and saving its contents as a .lc fits file
		print "downloading "+grb_name+" as sw"+trigger_id+"b_4chan_64ms.lc"
		urllib.urlretrieve(url, 'fits_files/'+"sw"+trigger_id+"b_4chan_64ms.lc")