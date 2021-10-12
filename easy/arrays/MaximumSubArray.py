def solution(nums):
    result = float('-inf')

    for i in range(0, len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            result = max(result, current_sum)

    return result

def solutionDP(nums):
    currentSubArray = nums[0]
    maxSubArray = nums[0]

    for i in range(1, len(nums)):
        currentSubArray = max(nums[i], currentSubArray + nums[i])
        maxSubArray = max(maxSubArray, currentSubArray)

    return maxSubArray

print(solutionDP([-2,-1,-3,4,-1,2,1,-5,4]))
print(solutionDP([1]))
print(solutionDP([5,4,-1,7,8]))
print(solutionDP([-2,1]))