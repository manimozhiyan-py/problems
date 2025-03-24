# reverse number

def reverse(number):
    reverse = 0
    while number:
        reverse *= 10
        reverse += number % 10
        number = number//10
    return reverse

print(reverse(1000))