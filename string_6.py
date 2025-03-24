def remove_not_alpha(string):
    str.upper(string)
    new_string=""
    for char in string:
        if (ord(char) >= 65 and ord(char) < 91) or (ord(char) > 89 and ord(char) < 123):
            new_string += char

    return new_string


print(remove_not_alpha("Abdj! ki"))