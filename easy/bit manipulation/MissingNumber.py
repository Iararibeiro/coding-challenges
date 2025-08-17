"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
"""

from typing import List


def missingNumber(nums: List[int]) -> int:
    """
    Explanation: 
    - xor number with 0 return the same number
    - xor same numbers will be zero
    - xor 2 different numbers returns 
    """
    
    ans = 0
    for i in range(1, len(nums) + 1):
        ans = ans ^ i

    for num in nums:
        ans = ans ^ num

    return ans


assert missingNumber([3,0,1]) == 2
assert missingNumber([0,1]) == 2
assert missingNumber([9,6,4,2,3,5,7,0,1]) == 8