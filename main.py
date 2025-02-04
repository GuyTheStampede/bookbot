with open("./books/frankenstein.txt") as f:
	file_text = f.read()
	character_dict = {}
	text_as_list = file_text.split()
	for x in file_text:
		x = x.lower()
		if x not in character_dict:
			character_dict[x] = 1
		else:
			character_dict[x] += 1
		
	print (character_dict)