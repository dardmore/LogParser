date = []					# Create date array
ip = []						# Create ip array
state = []					# Create state array
counter = []					# Create counter array

f = open("logfile.txt",'r')			# Open logfile.txt

text = f.readline()				# Read First line of file [which does not have any relevant data]
text = f.readline()				# Get next line of file, split the text and append the text into the data arrays
list = text.split("\t")				# Split text by 'tab'
date.append(list[0])		
ip.append(list[1])
state.append(list[3])
counter.append(1)

while True:
	text = f.readline()			# Read next line of file
	if (text == ""):			# If no new data, break while loop
		break				# End of file, break While Loop
	else:
		list = text.split("\t")		# Split line string using tab character
		i = 0
		found = False
		for j in date:
			if list[0] == date[i] and list[1] == ip[i] and list[3].rstrip('\n') == state[i].rstrip('\n'):		# Value is a repeat, Increase counter
				counter[i] = counter[i] + 1
				found = True
				break
			i += 1
		if not found:			# Create a New Entry
			date.append(list[0])		
			ip.append(list[1])
			state.append(list[3])
			counter.append(1)

i = 0
for j in date:
	print date[i], " ", ip[i], " ", state[i].rstrip('\n'), " ", counter[i]
	i += 1