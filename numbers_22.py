#strong number

number = 123

def fact(digit):
    factorial = 1
    for i in range(1, digit+1):
        factorial *= i
    return factorial


def strong(number):
    sum = 0
    numb = number
    while numb:
        digit = numb %10
        sum += fact(digit)
        numb //= 10
    return sum == number

print(strong(number))
