"""
You are given a 0-indexed array of integers nums of length n. 
You are initially positioned at index 0.
Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are 
generated such that you can reach index n - 1.
"""

from typing import List


def jump(nums: List[int]) -> int:
    jumps = 0
    current_reach = 0
    farthest_reach = 0

    for i, jump_power in enumerate(nums):
        potential_reach = i + jump_power
        farthest_reach = max(farthest_reach, potential_reach)

        if current_reach == i and i != len(nums) - 1:
            jumps += 1
            current_reach = farthest_reach
        
    return jumps

assert jump([2,3,1,1,4]) == 2
assert jump([2,3,0,1,4]) == 2