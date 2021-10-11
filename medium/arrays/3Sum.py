def solution(nums):
    result = []

    if len(nums) < 3:
        return result
    
    for i in range(0, (len(nums) - 2)):
        sum = nums[i]
        for j in range(i+1, (len(nums) - 1)):
            #sum = sum + nums[j]
            for k in range(j+1, (len(nums))):
                if sum + nums[j] + nums[k] == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    triplet.sort()

                    if (triplet not in result):
                        result.append(triplet)
    
    return result

print(solution([-1, 0, 1, 2, -1, -4]))

