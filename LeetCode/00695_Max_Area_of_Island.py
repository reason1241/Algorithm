# Time Complexity O(mn) 140 ms
# Space Complexity O(mn) 16.5 MB
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def sink(y: int, x: int) -> int:
            if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] == 0: return 0

            grid[y][x] = 0
            result = 1
            result += sink(y + 1, x)
            result += sink(y - 1, x)
            result += sink(y, x + 1)
            result += sink(y, x - 1)
            return result
        
        
        for y, row in enumerate(grid):
            for x, v in enumerate(row):
                if v:
                    area = sink(y, x)
                    grid[y][x] = area
                
        return max(col for row in grid for col in row)

# # Time Complexity O(mn) 152 ms
# # Space Complexity O(mn) 16.5 MB
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         def sink(y: int, x: int) -> int:
#             if not (0 <= y < len(grid) and 0 <= x < len(grid[0])) or grid[y][x] == 0: return 0
#             grid[y][x] = 0
#             return 1 + sink(y + 1, x) + sink(y - 1, x) + sink(y, x + 1) + sink(y, x - 1)
        
#         for y, row in enumerate(grid):
#             for x, v in enumerate(row):
#                 if v: grid[y][x] = sink(y, x)
                
#         return max(col for row in grid for col in row)

# # Time Complexity O(mn) 144 ms
# # Space Complexity O(mn) 16.5 MB
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         def sink(y: int, x: int) -> int:
#             if not (0 <= y < len(grid) and 0 <= x < len(grid[0])) or grid[y][x] == 0: return 0
#             grid[y][x] = 0
#             return 1 + sink(y + 1, x) + sink(y - 1, x) + sink(y, x + 1) + sink(y, x - 1)
        
#         ans = 0
#         for y, row in enumerate(grid):
#             for x, v in enumerate(row):
#                 if v: 
#                     ans = max(ans, sink(y, x))
                
#         return ans