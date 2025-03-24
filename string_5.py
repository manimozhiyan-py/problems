def remove_spaces(string):
    new_string = ""
    for char in string:
        if char == ' ':
            pass
        else:
            new_string += char

    return new_string

print(remove_spaces("hi gh"))