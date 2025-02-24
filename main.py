#print ("greetings boots")
'''
#this set of code is for CH2 L3
def main():
    	
	def get_book_text():
		with open("./books/frankenstein.txt") as f:
			return f.read()
	
	print (get_book_text())

main()
'''


'''
#this set of code is for CH2 L4
def main():
    	
	def get_book_text():
		with open("./books/frankenstein.txt") as f:
			return f.read()
	
	def word_count():
		word_count = 0
		all_words = get_book_text().split()
		for word in all_words:
			word_count += 1
		return word_count
	print (f"{word_count()} words found in the document")

main()
'''
import sys
if len(sys.argv) != 2:
	print("Usage: python main.py <file>")
	sys.exit(1)
from stats import report
report(sys.argv[1])