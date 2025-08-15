"""
Given an integer array nums, return true if any value appears at least twice 
in the array, and return false if every element is distinct.
"""

from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    values = {}

    for num in nums:
        if num in values.keys():
            return True
        else:
            values[num] = True

    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))