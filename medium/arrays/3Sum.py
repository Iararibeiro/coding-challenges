"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""


from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    result = []

    if len(nums) < 3:
        return result
    
    # 1 - sort the array
    nums.sort()

    # 2 - iterate over the array
    for i in range(0, len(nums) - 2):      
        # set the pointers
        left = i + 1
        right = len(nums) - 1

        if i > 0 and nums[i] == nums[i-1]:
            continue

        while left < right:
            sum_triplet = nums[i] + nums[left] + nums[right]

            if sum_triplet < 0:
                left += 1
            elif sum_triplet > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
    return result

assert threeSum([-1,0,1,2,-1,-4]) == [[-1, -1, 2], [-1, 0, 1]]
assert threeSum([0,1,1]) == []
assert threeSum([0,0,0]) == [[0,0,0]]
