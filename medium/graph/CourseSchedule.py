"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you 
must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""


from typing import List
from collections import defaultdict, deque

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    indegree = [0] * numCourses # visited array

    # build the graph first
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1
    
    # add to the queue the courses that dont need a prerequisite
    q = deque([i for i in range(numCourses) if indegree[i] == 0])

    # how many courses we finished so far
    taken = 0

    # bfs algorithm
    while q:
        course = q.popleft()
        taken += 1

        for nxt in graph[course]:
            indegree[nxt] -= 1 # mark as visited

            if indegree[nxt] == 0:
                q.append(nxt) 
    
    return taken == numCourses

assert canFinish(2, [[1,0]]) == True
assert canFinish(2, [[1,0],[0,1]]) == False