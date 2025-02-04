with open("./books/frankenstein.txt") as f:
	file_text = f.read()
	character_dict = {}
	text_as_list = file_text.split()
	print ("--- Begin report of books/frankenstein.txt ---")
	print (f"{len(text_as_list)} words found in the document")
	for x in file_text:
		x = x.lower()
		if x not in character_dict:
			character_dict[x] = 1
		else:
			character_dict[x] += 1
	for y in character_dict:
		#print (character_dict[y])
		if y == " " or y == "." or y == "#":
			pass
		else:
			print (f"The '{y}' character was found {character_dict[y]} times")
	print ("--- End report ---")