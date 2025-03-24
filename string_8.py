def remove_algebra(string):
    braces = ['[',']','{','}','(',')']
    result = ''
    for char in string:
        if char not in braces:
            result += char

    return result

print(remove_algebra("(a + b) * [c - d]"))

