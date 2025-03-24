def captilize(string):
    result = ""
    for index in range(len(string)):
        if index == 0 or index == len(string)-1:
            result += str.capitalize(string[index])

        else:
            result += string[index]


    return result


print(captilize("mani"))