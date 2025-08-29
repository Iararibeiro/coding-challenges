"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

from typing import List


def longestConsecutive(nums: List[int]) -> int:
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)

    nums.sort()

    max_sequence = 1
    current_sequence = 1

    for index in range(len(nums) - 1):
        if nums[index + 1] - nums[index] == 1:
            current_sequence += 1
            max_sequence = max(max_sequence, current_sequence)
        else:
            if nums[index + 1] != nums[index]:
                current_sequence = 1

    return max_sequence

assert longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
assert longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
assert longestConsecutive([1,0,1,2]) == 3