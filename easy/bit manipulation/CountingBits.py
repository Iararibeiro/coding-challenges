"""
Given an integer n, return an array ans of length n + 1 such that for each 
i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""

def countBits(n: int) -> list[int]:
    ans = [0] * (n + 1)

    for i in range(1,n + 1):
        # check for odd number
        if i % 2 == 0:
            index = i//2
            ans[i] = ans[index]
        else:
            ans[i] = ans[i-1] + 1
    return ans

assert countBits(2) == [0,1,1]
assert countBits(5) == [0,1,1,2,1,2]