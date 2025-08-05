def word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        word_array = file_contents.split()
    return len(word_array)

def character_count(path_to_file):
    character_dict = {}

    with open(path_to_file) as f:
        file_contents = f.read()
        lowercase_text = file_contents.lower()
        for i in lowercase_text:
            if i in character_dict:
                character_dict[i] += 1
            else:
                character_dict[i] = 1
    return character_dict

def sort_on(items):
    return items["num"]

def list_sort(path_to_file):
    character_dict = character_count(path_to_file)
    
    dict_list = []
    char = list(character_dict.keys())
    num = list(character_dict.values())
    entries = len(character_dict)
    for i in range(0, entries):
        dict = {}
        dict["char"] = char[i]
        dict["num"] = num[i]
        dict_list.append(dict)
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list


#def main():
    #sorted = list_sort("books/frankenstein.txt")
    #print(sorted)

#main()