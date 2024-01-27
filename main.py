def main():
    letter_dictionary = {}
    book_path = "books/frankenstein.txt"
    isalpha_list = []
    
    # this is the first line in the output before i run any code to print anything to the console
    print ("--- Begin report of books/frankenstein.txt ---")

    # this is the raw readout of the book in full
    with open(book_path) as b:
        book_contents = b.read()
        #print (book_contents)
    
    # this is putting individual letters from the book into the letter_dictionary dictionary
    for b in book_contents.lower():
        if b not in letter_dictionary:
            letter_dictionary[b] = 1
        elif b in letter_dictionary:
            letter_dictionary[b] += 1
        #print (b)
    
    #this is to print my next line of data to output to the console
    print (f"{len(book_contents.split())} words found in the document \n")
    
    #this is to place each alphabet letter entry of letter_dictionary into a list
    for character in letter_dictionary:
        if character.isalpha():
            tuple_to_append = character, letter_dictionary[character]
            isalpha_list.append(tuple_to_append)
    
    #this is to sort the new alpha list by the largest number of times the letter was recorded from letter_dictionary
    isalpha_list.sort(key=lambda tuple: tuple[1], reverse=True)        
    
    #this is to print each item in the newly sorted isalpha_list
    for i in isalpha_list:
        print (f"The '{i[0]}' character was found {i[1]} times")

    

main()