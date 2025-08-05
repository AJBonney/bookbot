def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

from stats import word_count
from stats import list_sort

def main():
    import sys

    if len(sys.argv) == 2:
        file_path = str(sys.argv[1])
        #print(file_path)
        word_count_total = word_count(file_path)
        dict_list = list_sort(file_path)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count_total} total words")
        print("--------- Character Count -------")
        for i in dict_list:
            char = i["char"]
            num = i["num"]
            if i["char"].isalpha() == True:
                print(f"{char}: {num}")
            else:
                pass
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()