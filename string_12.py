def case(string):
    result =''
    for char in string:
        if ord(char) > 64 and ord(char) < 91:
            result += chr(ord(char) + 32)
        if ord(char) > 96 and ord(char) < 123:
            result += chr(ord(char) -32)

    return result


print(case("AbCd"))

