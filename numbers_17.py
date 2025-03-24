# fibonacci

number = 7

def fibonacci(number):
    first =0
    second = 1
    #print(f'{first}, {second}, ', end='')
    for _ in range(number):
        print(f'{first}, ')
        first, second = second, second + first


fibonacci(number)