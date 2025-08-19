import sys
from stats import count_words
from stats import character_dict
from stats import create_report

def get_book_text(filepath):
    with open(filepath) as fp:
        contents = fp.read()
        return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    book = get_book_text(path)
    
    character_dictionary = character_dict(book)
    ordered_list_of_characters = create_report(character_dictionary)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    count_words(book)
    print("--------- Character Count -------")
    for dictionary in ordered_list_of_characters:
        keys = dictionary.keys()
        line = ""

        for key in keys:
            if key == "char":
                line += f"{dictionary[key]}: "
            if key == "num":
                line += f"{dictionary[key]}"
        print(line)
    print("============= END ===============")
    
main()
