def searchInsert(nums, target):
    if len(nums) == 1:
        if target < nums[0] : return 0
        if target > nums[0] : return 1

    halfPoint = len(nums)/2
    if nums[halfPoint] == target: return halfPoint

    #check if the target is bigger then the middle
    if (nums[halfPoint] > target) :
        return searchInsert(nums[0:halfPoint], target)
    else :
        return searchInsert(nums[halfPoint:], target)    


#Input: nums = [1,3,5,6], target = 5, Output: 2
#print(searchInsert([1,3,5,6], 5))
#Input: nums = [1,3,5,6], target = 2, Output: 1
#print(searchInsert([1,3,5,6], 2))
#Input: nums = [1,3,5,6], target = 7, Output: 4
print(searchInsert([1,3,5,6], 7))
#Input: nums = [1,3,5,6], target = 0, Output: 0
#searchInsert([1,3,5,6], 0)
#Input: nums = [1], target = 0, Output: 0
#searchInsert([1], 0)
