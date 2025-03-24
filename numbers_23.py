# Automorphic number

n = 12

def automorphic(number):
    square = str(number ** 2)
    number = str(number)
    #print(square[-2::])
    if number == square[-len(number)::]:
        return True
    return False

print(automorphic(n))