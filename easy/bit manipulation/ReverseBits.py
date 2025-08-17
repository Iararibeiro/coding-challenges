"""
Reverse bits of a given 32 bits unsigned integer.

Note:
Note that in some languages, such as Java, there is no unsigned integer type.
In this case, both input and output will be given as a signed integer type. 
They should not affect your implementation, as the integer's internal binary 
representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation.
"""

def reverseBits(n: int) -> int:
    res = 0
    n &= 0xFFFFFFFF

    for _ in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1

    return res & 0xFFFFFFFF

assert reverseBits(43261596) == 964176192
assert reverseBits(2147483644) == 1073741822