def enumerate_list(my_list):
    new_list = []
    i = 0
    for element in my_list:
        if element != "":
            new_elem = f"{i}. {element}"
            new_list.append(new_elem)
            i += 1

    return new_list


def enumerate_backwards(my_list):
    new_list = []
    i = 0
    for element in my_list:
        if element != "":
            word = element[:: -1]
            new_elem = f"{i}. {word}"
            new_list.append(new_elem)
            i += 1

    return new_list
