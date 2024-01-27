def main():
    final_results = {}
    book_path = "books/frankenstein.txt"
        
    with open(book_path) as b:
        book_contents = b.read()
        #print (book_contents)
    for b in book_contents.lower():
        if b not in final_results:
            final_results[b] = 1
        elif b in final_results:
            final_results[b] += 1
        #print (b)
    
    print (final_results)
    

main()