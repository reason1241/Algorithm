# Time Complexity O(mn) 172 ms
# Space Complexity O(mn) 14.4 MB
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        if k % (m * n) == 0: return grid
        
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                ny, nx = divmod(i * n + j + k, n)
                result[ny % m][nx] = grid[i][j]
        
        return result
    
    
# # Time Complexity O(mn) 172 ms
# # Space Complexity O(mn) 14.4 MB    
# class Solution:
#     def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
#         m, n = len(grid), len(grid[0])
        
#         k %= (m * n)
        
#         flat = [j for i in grid for j in i]
                
#         moved = flat[-k:] + flat[:-k]
                
#         return [moved[i * n : i * n + n] for i in range(m)]