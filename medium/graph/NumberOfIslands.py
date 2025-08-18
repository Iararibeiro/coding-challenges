"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and 
'0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands 
horizontally or vertically. You may assume all four edges of the grid are 
all surrounded by water.
"""

from typing import List

def numIslands(grid: List[List[str]]) -> int:
    def dfs(row, col):
      grid[row][col] = '0'

      for dx, dy in zip(directions[:-1], directions[1:]):
        new_row, new_col = row + dx, col + dy

        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == '1':
           dfs(new_row, new_col)
        

    rows = len(grid)
    cols = len(grid[0])

    island_count = 0
    directions = (-1, 0, 1, 0, -1)


    for row in range(0,rows):
      for col in range(0, cols):
        if grid[row][col] == '1':
            dfs(row, col)
            island_count += 1

    return island_count


assert numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]) == 1
assert numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]) == 3
