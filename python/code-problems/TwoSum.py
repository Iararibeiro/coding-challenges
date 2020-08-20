def twoSum(self, nums: List[int], target: int) -> List[int]:
    dictionary = {}
    answer = []

    for i in range(len(nums)):
        secondNumber = target-nums[i]
        if(secondNumber in dictionary.keys()):
            secondIndex = nums.index(secondNumber)
            if(i != secondIndex):
                return sorted([i, secondIndex])

        dictionary.update({nums[i]: i})

print twosum([2,7,11,15], 9)
print twosum([0,1,2,3,4], 4)
print twosum([1,3,4,5,0], 1)
