# Time Complexity O(n) 836 ms
# Space Complexity O(1) 16.1 MB	
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def sink(y: int, x:int) -> int:
            if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]): return -1
            if grid[y][x] == 0: return 0
            
            grid[y][x] = 0
            
            next_step = [sink(y + 1, x), sink(y - 1, x), sink(y, x - 1), sink(y, x + 1)]

            if all([step >= 0 for step in next_step]):
                return sum(next_step) + 1
            return -1
        
        ans = 0
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if col:
                    result = sink(y, x)
                    ans += result if result > 0 else 0
        return ans

# Time Complexity O(n) 533 ms
# Space Complexity O(1) 16 MB	    
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def sink(y: int, x:int):
            if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] == 0: return
            grid[y][x] = 0
            all([sink(y + 1, x), sink(y - 1, x), sink(y, x - 1), sink(y, x + 1)])

        y_len, x_len = len(grid), len(grid[0])
        
        for y in range(y_len):
            sink(y, 0)
            sink(y, x_len - 1)
            
        for x in range(x_len):
            sink(0, x)
            sink(y_len - 1, x)
        
        return sum(sum(row) for row in grid)