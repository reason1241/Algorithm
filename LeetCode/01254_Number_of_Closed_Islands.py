# Time Complexity O(n) 136 ms
# Space Complexity O(n) 14.5 MB
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def sink(y:int, x:int) -> bool:
            if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]): return False
            if grid[y][x] == 1: return True
            grid[y][x] = 1
            return all([sink(y+1,x),sink(y-1,x),sink(y,x+1),sink(y, x-1)])
        
        ans = 0
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if not grid[y][x] and sink(y,x):
                    ans += 1
        return ans