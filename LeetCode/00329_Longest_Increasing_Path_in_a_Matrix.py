# Time Complexity O(mn) 522 ms
# Sapce Complexity O(mn) 14.7 MB
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        depths = [[-1] * n for _ in range(m)]
        
        def dp_dfs(y: int, x: int) -> int:
            if depths[y][x] != -1:
                return depths[y][x]
            
            depths[y][x] = 1
            
            for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
                if 0 <= y+dy < m and 0 <= x+dx < n and matrix[y+dy][x+dx] > matrix[y][x]:
                    depths[y][x] = max(dp_dfs(y+dy, x+dx) + 1, depths[y][x])
            
            return depths[y][x]
            
        return max(dp_dfs(y, x) for y in range(m) for x in range(n))
                