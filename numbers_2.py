# Finding palindrome within range

L, R = 1, 200

def palindrome(L, R):
    output = []
    for num in range(L, R+1):
        if str(num) == str(num)[::-1]:
            output.append(num)


def gene_palindrome(L, R):
    palindromes = []

    def creation(num, odd):
        if odd:
            return int(str(num) + str(num)[-2::-1])
        else:
            return int(str(num) + str(num)[::-1])

    num = 1
    while True:
        for odd in [True, False]:
            half =  creation(num, odd)
            if half > R:
                return palindromes
            if half >= L:
                palindromes.append(half)
        num += 1

print(gene_palindrome(L, R))