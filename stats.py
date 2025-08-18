from operator import itemgetter

def count_words(text):
    count = len(text.split())
    print(f"Found {count} total words")

def character_dict(text):
    c_dict = {}
    char_list = list(text)

    for character in char_list:
        character = character.lower()
        if character in c_dict:
            c_dict[character] += 1
        else:
            c_dict[character] = 1

    return c_dict

def create_report(dictionary):
    new_list = []
    # need to create multiple dictionaries
    for k, v in dictionary.items():
        if k.isalpha():
            new_list.append({'char': k, 'num': v})
    #sorting
    new_list = sorted(new_list, key=itemgetter('num'), reverse=True)
    
    return new_list