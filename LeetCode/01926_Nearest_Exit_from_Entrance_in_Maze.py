from collections import deque
# Time Complexity O(mn) 788 ms
# Space Complexity O(mn) 14.5 MB
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:       
        m, n = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = "+"
        q = deque([(entrance[0], entrance[1], 0)])
        
        while q:
            y, x, d = q.popleft()
            if (y == 0 or y == (m - 1) or x == 0 or x == (n - 1)) and [y, x] != entrance:
                return d

            for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                if 0 <= y+dy < m and 0 <= x+dx < n and maze[y+dy][x+dx] == ".":
                    q.append((y+dy, x+dx, d + 1))
                    maze[y+dy][x+dx] = '+'
            
        return -1
                    
