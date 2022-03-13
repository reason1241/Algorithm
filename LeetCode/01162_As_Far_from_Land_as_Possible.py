# Time Complexity O(n**2) 1300 ms
# Space Complexity O(n**2) 17.3 MB
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = []
        visited = set()
        
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val:
                    q.append(((y, x), 0))
        
        max_dist = 0
        
        while q:          
            pos, dist = q.pop(0)
            if pos in visited:
                continue
            visited.add(pos)
            
            y, x = pos
        
            if y > 0 and (y - 1, x) not in visited: q.append(((y - 1, x), dist + 1))
            if y < n - 1 and (y + 1, x) not in visited: q.append(((y + 1, x), dist + 1))
            if x > 0 and (y, x - 1) not in visited: q.append(((y, x - 1), dist + 1))
            if x < n - 1 and (y, x + 1) not in visited: q.append(((y, x + 1), dist + 1))
            
            max_dist = dist if dist > max_dist else max_dist
        
        return max_dist if max_dist > 0 else -1
    
# Time Complexity O(n**2) 2492 ms
# Space Complexity O(n**2) 17.1 MB
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = []
        
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val:
                    q.append(((y, x), 0))
        
        max_dist = 0
        
        while q:
            pos, dist = q.pop(0)
            y, x = pos
            
            if grid[y][x] == 2:
                continue
            
            grid[y][x] = 2
            
            if y > 0: q.append(((y - 1, x), dist + 1))
            if y < n - 1: q.append(((y + 1, x), dist + 1))
            if x > 0: q.append(((y, x - 1), dist + 1))
            if x < n - 1: q.append(((y, x + 1), dist + 1))
            
            max_dist = dist if dist > max_dist else max_dist
        
        return max_dist if max_dist > 0 else -1
    

# Time Complexity O(n**2) 600 ms
# Space Complexity O(n**2) 15 MB    
# BFS
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        q = [(y,x) for y in range(n) for x in range(n) if grid[y][x]]
        
        depth = -1
        
        while q and len(q) != n ** 2:
            next_q = []
            
            for y, x in q:
                for n_y, n_x in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
                    if 0 <= n_y < n and 0 <= n_x < n and not grid[n_y][n_x]:
                        grid[n_y][n_x] = 1
                        next_q.append((n_y, n_x))
            
            q = next_q
            depth += 1
                
        return depth

    
# Time Complexity O(n**2) 593 ms
# Space Complexity O(n**2) 14.4 MB    
# DP
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        dp = [[float('inf')] * n for _ in range(n)]
        
        for y in range(n):
            for x in range(n):
                if grid[y][x]:
                    dp[y][x] = 0
                else:
                    up = dp[y - 1][x] if y > 0 else float('inf')
                    left = dp[y][x - 1] if x > 0 else float('inf')
                    dp[y][x] = min(up + 1, left + 1, dp[y][x])
        
        for y in range(n - 1, -1, -1):
            for x in range(n - 1, -1, -1):
                if grid[y][x]:
                    dp[y][x] = 0
                else:
                    down = dp[y + 1][x] if y < n - 1 else float('inf')
                    right = dp[y][x + 1] if x < n - 1 else float('inf')
                    dp[y][x] = min(down + 1, right + 1, dp[y][x])
        
        max_val = max(j for i in dp for j in i)
    
        return -1 if max_val in (0, float('inf')) else max_val
                
                
                