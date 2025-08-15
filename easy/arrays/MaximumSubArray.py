"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""

from typing import List


def maxSubArray(nums: List[int]) -> int:
    current_max = nums[0]
    global_max = nums[0]

    for i in range(1, len(nums)):
        current_max = max(nums[i], (current_max + nums[i]))
        global_max = max(current_max, global_max)

    return global_max

assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert maxSubArray([1]) == 1
assert maxSubArray([5,4,-1,7,8]) == 23