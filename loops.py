def index_of_by_index(word, list, index):
    i = 0
    new_list = list[index:]
    while i < len(new_list):
        current_word = new_list[i]
        if current_word == word:
            return i + index
        i += 1

    return -1

def index_of_empty(list):
    i = 0
    while i < len(list):
        current_index = list[i]
        if current_index == "":
            return i
        i += 1
    return -1

def index_of(word, list):
    i = 0
    while i < len(list):
        if word == list[i]:
            return i
        i += 1
    return -1


def put(word, list):
    i = 0
    for element in list:
        if element == "":
            list[i] = word
            return i
        i += 1
    return -1

def remove(word, list):
    removed_strings = 0
    for i in range(len(list)):
        if list[i] == word:
            list[i] = ""
            removed_strings += 1
    return removed_strings
