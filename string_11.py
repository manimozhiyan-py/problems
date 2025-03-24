def lexicographic(string):
    result = ""
    for char in string:
        if char == 'z' :
            result += chr(97)
        elif char == 'Z':
            result += chr(65)
        else:
            result += chr(ord(char)+1)

    return result

print(lexicographic("abadfasdfcdZ"))