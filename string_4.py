def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""
    for char in string:
        if char not in vowels:
            result += char

    return result


print(remove_vowels('abcd'))