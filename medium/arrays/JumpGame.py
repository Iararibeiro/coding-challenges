"""
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""

from typing import List


def canJump(nums: List[int]) -> bool:
    max_reach = 0

    for i, jump_power in enumerate(nums):
        potential_reach = i + jump_power

        if i > max_reach:
            return False
        
        max_reach = max(max_reach, potential_reach)

    return True


assert canJump([2,3,1,1,4]) == True
assert canJump([3,2,1,0,4]) == False
