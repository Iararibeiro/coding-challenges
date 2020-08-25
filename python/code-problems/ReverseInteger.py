import sys

def reverseInteger(number):
    rev = 0
    negativeNumber = False
    negLimit= -0x80000000
    posLimit= 0x7fffffff

    if (number < 0):
        negativeNumber = True
        number = number * -1

    while(number != 0):
        pop = number % 10
        number /= 10
        if (rev > sys.maxint) or (rev == sys.maxint/10 and pop > sys.maxint):
            return 0
        if (rev < -sys.maxint) or (rev == -sys.maxint/10 and pop < -sys.maxint):
            return 0
        rev = rev * 10 + pop

    if negativeNumber:
        rev = rev * -1
        if rev < negLimit:
            return 0
    return rev
        else:
        if rev > posLimit:
            return 0
        return rev

print reverseInteger(123)
print reverseInteger(-123)
print reverseInteger(1534236469)
