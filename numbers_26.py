#Harshad Number

n = 18

def harshad(number):
    sum = 0
    n = number
    while n:
        sum += n%10
        n //= 10
    return True if number % sum == 0 else False

print(harshad(n))