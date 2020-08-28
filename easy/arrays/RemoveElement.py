def removeElement(nums, val):
    count = 0

    for i in range(len(nums)):
        if nums[i] == val:
            j = len(nums) - 1
            while j != i:
                if nums[j] != val:
                    nums[i] = nums[j]
                    nums[j] = val
                    j = i
                else:
                    j = j - 1

    for i in nums:
        if i != val:
            count+=1

    return count

removeElement([3,2,2,3], 3)
removeElement([0,1,2,2,3,0,4,2], 2)
