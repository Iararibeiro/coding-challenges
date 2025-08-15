from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    p1 = 0 
    p2 = 1

    while p1 <= len(nums):
        if nums[p1] + nums[p2] == target:
            return [p1, p2]
        else:
            if p2 == len(nums) - 1:
                p1 = p1 + 1
                p2 = p1 + 1
            else:
                p2 = p2 + 1

assert twoSum([2,7,11,15], 9) == [0,1]
assert twoSum([3,2,4], 6) == [1,2]
assert twoSum([3,3],6) == [0,1]