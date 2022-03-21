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
        
        