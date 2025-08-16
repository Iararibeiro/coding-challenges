"""
Given an integer array nums, find a subarray that has the largest product,
and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
"""

from typing import List


def maxProduct(nums: List[int]) -> int:
    current_max = current_min = global_max = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            current_max, current_min = current_min, current_max

        current_max = max(nums[i], (current_max * nums[i]))
        current_min = min(nums[i], (current_min * nums[i]))
        global_max = max(current_max, global_max)

    return global_max

assert maxProduct([2,3,-2,4]) == 6
assert maxProduct([-2,0,-1]) == 0
assert maxProduct([2,3,-2,4]) == 6