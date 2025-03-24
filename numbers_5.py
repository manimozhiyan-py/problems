# amstrong number


def amstrong_number(ams):
    n = len(str(ams))
    amst = ams
    sum =0
    while amst:
        sum += (amst %10)**n
        amst = int(amst/10)

    return sum == ams

print(amstrong_number(123))
