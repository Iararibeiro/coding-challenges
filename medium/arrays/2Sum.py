def solution(nums, target):
    mapValues = {}
    result = []

    if len(nums) == 0:
        return result
    
    for i in range(0, len(nums)):
        x = target - nums[i]

        if mapValues.get(x) != None:
            result = [i, mapValues.get(x)]
        else: 
            mapValues[nums[i]] = i
 
    result.sort()
    return result


print(solution([2,7,11,15], 9))
print(solution([-1,-2,-3,-4,-5], -8))