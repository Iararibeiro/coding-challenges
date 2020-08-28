def removeDuplicates(nums) -> int:
    if len(nums) == 0: return 0

    elementCount = len(nums)
    index = 1
    
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[index] = nums[i]
            index += 1
    return index

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
