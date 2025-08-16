"""
Given an integer array nums, return an array answer such that answer[i] is 
equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 
32-bit integer.
You must write an algorithm that runs in O(n) time and without using the 
division operation.
"""

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    answer = []
    prefix_product = 1
    suffix_product = 1

    for index in range(0, len(nums)):
        answer.append(prefix_product)
        prefix_product = prefix_product * nums[index]
            

    for index in range(len(nums) -1, -1, -1):
        answer[index] = suffix_product * answer[index]
        suffix_product = suffix_product * nums[index]
        
    return answer


assert productExceptSelf([1,2,3,4]) == [24, 12, 8, 6]
assert productExceptSelf([1,1,0,-3,3]) == [0, 0, -9, 0, 0]