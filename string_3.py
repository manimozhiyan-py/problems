def ascii(string):
    ascii_list = []
    for i in string:
        ascii_list.append(ord(i))
    return ascii_list

print(ascii("abA"))