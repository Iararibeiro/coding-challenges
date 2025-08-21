"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific 
Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and
bottom edges.
The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights 
where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, 
south, east, and west if the neighboring cell's height is less than or equal to the current cell's 
height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can 
flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
"""

from typing import List

def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    queue_pacific = []
    queue_atlantic = []

    rows = len(heights)
    cols = len(heights[0])

    pacific_reachable = [[False for _ in range(cols)] for _ in range(rows)]
    atlantic_reachable = [[False for _ in range(cols)] for _ in range(rows)]
    
    directions = (-1, 0, 1, 0, -1)

    for r in range(0,rows):
        if [r,0] not in queue_pacific:
            queue_pacific.append([r,0])
        pacific_reachable[r][0] = True

        if [r,rows -1] not in queue_atlantic:
            queue_atlantic.append([r,rows - 1])
        atlantic_reachable[r][rows - 1] = True

    for c in range(0,cols):
        if [0, c] not in queue_pacific:
            queue_pacific.append([0,c])
        pacific_reachable[0][c] = True

        if [cols - 1,c] not in queue_atlantic:
            queue_atlantic.append([cols - 1,c])
        atlantic_reachable[cols - 1][c] = True

    pacific_reachable[0][0] = True
    atlantic_reachable[rows - 1][cols - 1] = True

    while queue_pacific:
        cell = queue_pacific.pop(0)
        r = cell[0]
        c = cell[1]

        current_height = heights[r][c]
        
        pacific_reachable[r][c] = True

        #check neighbors
        for dx, dy in zip(directions[:-1], directions[1:]):
            new_row, new_col = r + dx, c + dy

            if 0 <= new_row < rows and 0 <= new_col < cols and pacific_reachable[new_row][new_col] == False and current_height <= heights[new_row][new_col]:
                queue_pacific.append([new_row, new_col])
                pacific_reachable[new_row][new_col] = True
    
    while queue_atlantic:
        cell = queue_atlantic.pop(0)
        r = cell[0]
        c = cell[1]

        current_height = heights[r][c]
        
        atlantic_reachable[r][c] = True

        #check neighbors
        for dx, dy in zip(directions[:-1], directions[1:]):
            new_row, new_col = r + dx, c + dy

            if 0 <= new_row < rows and 0 <= new_col < cols and atlantic_reachable[new_row][new_col] == False and current_height <= heights[new_row][new_col]:
                queue_atlantic.append([new_row, new_col])
                atlantic_reachable[new_row][new_col] = True

    res = []
    for r in range(0,rows):
        for c in range(0, cols):
            if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                res.append([r,c])


    return res

assert pacificAtlantic(
    [[1,2,2,3,5],
     [3,2,3,4,4],
     [2,4,5,3,1],
     [6,7,1,4,5],
     [5,1,1,2,4]]
    ) == [
        [0,4],
        [1,3],
        [1,4],
        [2,2],
        [3,0],
        [3,1],
        [4,0]
    ]