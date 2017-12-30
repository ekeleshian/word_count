def word_count(string):
	current_idx = 0
	start_idx = 0
	current_idx = 0
	list_of_starts = []
	list_of_stops = []
	list_of_words = []
	word_count_dict = {}

	while current_idx <= len(string) - 2:
		if string[current_idx] == ' ':
			current_idx += 1
		elif (string[current_idx] != ' ') and (string[current_idx - 1] == ' ' or current_idx == 0) and (string[current_idx + 1]== ' '):
			start_idx = current_idx
			list_of_starts.append(start_idx)
			current_idx += 1
			stop_idx = current_idx
			list_of_stops.append(stop_idx)
		elif (string[current_idx] != ' ') and (string[current_idx - 1] == ' '):
			start_idx = current_idx
			list_of_starts.append(start_idx)
			current_idx += 1
		elif (current_idx < len(string) - 2)  and (string[current_idx] != ' ') and (string[current_idx + 1] == ' '):
			current_idx += 1
			stop_idx = current_idx
			list_of_stops.append(stop_idx)
		else:
			current_idx += 1
			

	if (current_idx == len(string) - 1) and (string[current_idx] != ' '):
		stop_idx = current_idx + 1
		list_of_stops.append(stop_idx)
		current_idx += 1


		
	start_stop = zip(list_of_starts, list_of_stops)

	for start, stop in start_stop:
		word = string[start: stop]
		list_of_words.append(word)



	for word in list_of_words:
		word = word.lower()
		if word not in word_count_dict:
			word_count_dict[word] = 1
		else:
			word_count_dict[word] += 1

	print(word_count_dict)

	return word_count_dict



word_count("I do      not like it Sam    I    Am")

	
