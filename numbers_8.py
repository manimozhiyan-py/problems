#check positive or negative

def pos_neg(number):
    if number == 0:
        return f'zero'
    return f'Positive' if number >0 else f'Negative'

print(pos_neg(0))