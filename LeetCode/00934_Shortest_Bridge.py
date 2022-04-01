# Time Complexity O(n**2) 524 ms
# Space Complexity O(n**2) 16.5 MB
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # the islands should be 1 -> 2, 3
        def dfs(y: int, x: int, label: int):
            if 0 <= y < len(grid) and 0 <= x < len(grid):
                if grid[y][x] == 0 or grid[y][x] > 1: return
                
                grid[y][x] = label
                
                for dy, dx in (1,0),(-1,0),(0,1),(0,-1):
                    dfs(y + dy, x + dx, label)
        
        label = 2
        for y in range(len(grid)):
            for x in range(len(grid)):
                if grid[y][x] == 1:
                    dfs(y, x, label)
                    label += 1
        
        q = [(y, x, 0) for y in range(len(grid)) for x in range(len(grid)) if grid[y][x] == 2]
        
        while q:
            next_q = []
            for y, x, d in q:
                for dy, dx in (1,0),(-1,0),(0,1),(0,-1):
                    if 0 <= y+dy < len(grid) and 0 <= x+dx < len(grid):
                        if grid[y+dy][x+dx] == 3:
                            return d
                        if grid[y+dy][x+dx] == 0:
                            next_q.append((y+dy, x+dx, d+1))
                            grid[y+dy][x+dx] = 2
            q = next_q
        
        return -1
    
    
# from itertools import product
# # Time Complexity O(n**2) 460 ms
# # Space Complexity O(n**2) 16.7 MB
# class Solution:
#     def shortestBridge(self, grid: List[List[int]]) -> int:
#         q = []
        
#         # the islands should be 1 -> 2
#         def dfs(y: int, x: int, label: int):
#             if 0 <= y < len(grid) and 0 <= x < len(grid):
#                 if grid[y][x] == 0 or grid[y][x] > 1: return
                
#                 grid[y][x] = label
#                 q.append((y, x))
                
#                 for dy, dx in (1,0),(-1,0),(0,1),(0,-1):
#                     dfs(y + dy, x + dx, label)
        
#         for y, x in product(range(len(grid)), range(len(grid))):
#             if grid[y][x] == 1:
#                 dfs(y, x, 2)
#                 break
        
#         d = 0
#         while q:
#             for _ in range(len(q)):
#                 y, x = q.pop(0)
#                 for dy, dx in (1,0),(-1,0),(0,1),(0,-1):
#                     if 0 <= y+dy < len(grid) and 0 <= x+dx < len(grid):
#                         if grid[y+dy][x+dx] == 1:
#                             return d
#                         if grid[y+dy][x+dx] == 0:
#                             q.append((y+dy, x+dx))
#                             grid[y+dy][x+dx] = 2
#             d += 1
#         return -1