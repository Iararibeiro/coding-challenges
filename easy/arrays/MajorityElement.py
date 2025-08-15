"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than [n/2] times.
You may assume that the majority element always exists in the array.
"""

from typing import List
import math

def majorityElement(nums:List[int]) -> int:
    MIN_OCCURENCY = math.ceil(len(nums) / 2)
    count_dict = {} 

    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1

        if count_dict[num] >= MIN_OCCURENCY:
            return num 

# input 1
nums = [3,2,3]
assert majorityElement(nums) == 3

# input 2
nums = [2,2,1,1,1,2,2]
assert majorityElement(nums) == 2
