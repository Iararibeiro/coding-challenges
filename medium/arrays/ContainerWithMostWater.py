"""
You are given an integer array height of length n. There are n vertical lines drawn such that the 
two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container 
contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""

from typing import List


def maxArea(height: List[int]) -> int:
    result = 0
    n = len(height) - 1
    p1 = 0
    p2 = n

    while n > 0:
        containerHeight = min(height[p1], height[p2])
        area = containerHeight * n

        if area > result:
            result = area
        
        if height[p1] < height[p2]:
            p1+=1
        else:
            p2-=1
        
        n -= 1

    return result

assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert maxArea([1,1]) == 1
assert maxArea([4,3,2,1,4]) == 16
assert maxArea([1,2,1]) == 2