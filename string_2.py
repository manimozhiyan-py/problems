def count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    space_char,vowels_char,consonent_char = 0,0,0
    for char in string:
        if char == " ":
            space_char += 1
        else:
            if char in vowels:
                vowels_char += 1
            else:
                consonent_char += 1

    return space_char,vowels_char,consonent_char

print(count("hi bye"))
