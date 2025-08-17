"""
Given two integers a and b, return the sum of the two integers 
without using the operators + and -.
"""

def getSum(a: int, b:int) -> int:
    # 32-bit mask (all 1s)
    mask = 0xFFFFFFFF
    # Max positive int in 32 bits
    MAX = 0x7FFFFFFF

    while b != 0:
        partial_sum = (a ^ b) & mask
        carry_on = ((a & b) << 1) & mask

        a = partial_sum
        b = carry_on
    
    # If result is within positive range, return as is
    if a <= MAX:
        return a
    else:
        # Convert from two's complement to Python negative int
        return ~(a ^ mask)

getSum(-1, 1)

# assert getSum(1,2) == 3
# assert getSum(2,3) == 5
# assert getSum(5,3) == 8