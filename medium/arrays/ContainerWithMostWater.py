def maxArea(height):
    result = 0

    for i in range(0, len(height)):
    
        for j in range(i+1, len(height)):
            if height[i] <= height[j]:
                containerHeight = height[i]
            else:
                containerHeight = height[j]
            lenght = j - i
            
            area = containerHeight * lenght
            if area > result:
                result = area

    print(result)



maxArea([1,8,6,2,5,4,8,3,7])
maxArea([1,1])
maxArea([4,3,2,1,4])
maxArea([1,2,1])