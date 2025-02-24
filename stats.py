def get_book_text():
    with open() as f:
        return f.read()
	
def word_count():
    word_count = 0
    all_words = get_book_text().split()
    for word in all_words:
        word_count += 1
    return word_count

#this set of code is for CH3 L1
def report(book):    
    with open(book) as f:
        print ("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        file_text = f.read()
        character_dict = {}
        text_as_list = file_text.split()
        print ("----------- Word Count ----------")
        print (f"Found {len(text_as_list)} total words")
        print ("--------- Character Count -------")
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
                print (f"{y}: {character_dict[y]}")
        print ("============= END ===============")

#print (f"{word_count()} words found in the document")