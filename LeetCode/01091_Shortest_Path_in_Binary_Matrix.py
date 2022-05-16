# Time Complexity O(n**2) 740 ms
# Space Complexity O(n) 14.4 MB
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int: 
        if grid[0][0] or grid[-1][-1]: return -1
        
        moves = [(y, x) for y in (1,0,-1) for x in (1,0,-1) if (y,x) != 0]
        
        n = len(grid)
        
        q, level = [(0, 0)], 0
        
        while q:
            next_q = []
            
            while q:
                y, x = q.pop(0)
               
                if grid[y][x]: continue
                
                grid[y][x] = 1
                
                if y == n - 1 and x == n - 1:
                    next_q = []
                    break
                
                for dy, dx in moves:
                    if ((0 <= y + dy <= n-1) 
                        and (0 <= x + dx <= n-1) 
                        and not grid[y + dy][x + dx]):
                        next_q.append((y + dy, x + dx))
            level += 1
            q = next_q
            
        return level if grid[n-1][n-1] else -1

# # Time Complexity O(n**2) 1120 ms
# # Space Complexity O(n) 14.3 MB
# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         if grid[0][0] == 1 or grid[n-1][n-1] == 1: return -1
        
#         q = [(0,0)]
        
#         level = 0
        
#         while q:
#             level += 1
#             for _ in range(len(q)):
#                 y, x = q.pop(0)
#                 if y == n-1 and x == n-1: return level
                
#                 for dy, dx in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
#                     if 0 <= y+dy < n and 0 <= x+dx < n and grid[y+dy][x+dx] == 0:
#                         q.append((y+dy, x+dx))
#                         grid[y+dy][x+dx] = 1
                
#         return -1
        