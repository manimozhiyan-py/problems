#Factorial number

n = 5

def factorial(number):
    fact = 1
    while number:
        fact *= number
        number -= 1
    return fact

print(factorial(n))