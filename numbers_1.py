#Palindrome or not

def palindrome(n):
    return str(n) == str(n)[::-1]


print(palindrome(121))