import sys
from stats import words
from stats import count_letters
from stats import sorted_letters

def get_book_text(t):
    with open(t) as f:
        file_contents = f.read()
    return file_contents
   
def main():
    if len(sys.argv) == 2:
    
        book = get_book_text(sys.argv[1])
    
        count = words(book)
        number_of_letters = count_letters(book)
        final = sorted_letters(number_of_letters)
        #print(f"{count} words found in the document")
        #print(number_of_letters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {count} total words")
        print("--------- Character Count -------") 
        for item in final:
            char = item["char"]
            count = item["num"]
            print(f"{char}: {count}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()







