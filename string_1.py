def palindrome(string):
    return string == string[::-1]

def using_for(string):
    no_of_char = len(string) -1
    for index in range(int(len(string)/2)):
        if string[index] == string[no_of_char - index]:
            return False 
    return True
        
        
print(palindrome("tenet"))
