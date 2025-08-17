"""
Given a positive integer n, write a function that returns the number of set bits in its binary 
representation (also known as the Hamming weight).
"""


def hammingWeight(n: int) -> int:
    count = 0

    while n > 0:
        # Check if the last bit is 1
        if n & 1:
            count += 1
        
        # Shift right by one bit
        n >>= 1

    return count

assert hammingWeight(11) == 3
assert hammingWeight(128) == 1
assert hammingWeight(2147483645) == 30