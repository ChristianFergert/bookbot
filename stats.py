def get_word_count(text):
    wordlist = text.split()
    return len(wordlist)

def get_character_counts(text):
    text = text.lower()
    character_count = {}
    for character in text:
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count

def sort_dict(dict):
    dict_list = []
    for char in dict:
        tempdict = {}
        tempdict["char"] = char
        tempdict["num"] = dict[char]
        dict_list.append(tempdict)
    def sort_key_num(list):
        return list["num"]
    dict_list.sort(reverse=True, key=sort_key_num)
    return dict_list
    
    
