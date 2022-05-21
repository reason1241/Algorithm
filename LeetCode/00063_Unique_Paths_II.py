# Time Complexity O(mn) 47 ms
# Space Complexity O(mn) 14 MB
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1: return 0
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
                
        for y in range(m):
            for x in range(n):
                up = dp[y-1][x] if 0 <= y-1 < m and 0 <= x < n and obstacleGrid[y-1][x] == 0 else 0
                left = dp[y][x-1] if 0 <= y < m and 0 <= x-1 < n and obstacleGrid[y][x-1] == 0  else 0
                dp[y][x] += up + left
                
        return dp[m-1][n-1]
    
# # Time Complexity O(mn) 50 ms
# # Space Complexity O(mn) 14.1 MB    
# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m, n = len(obstacleGrid), len(obstacleGrid[0])
        
#         if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1: return 0
        
#         dp = [[0] * n for _ in range(m)]
        
#         for x in range(n):
#             if obstacleGrid[0][x] == 1:
#                 break
#             dp[0][x] = 1
            
#         for y in range(m):
#             if obstacleGrid[y][0] == 1:
#                 break
#             dp[y][0] = 1
                
#         for y in range(1, m):
#             for x in range(1, n):
#                 if obstacleGrid[y][x] == 0:
#                     dp[y][x] = dp[y-1][x] + dp[y][x-1]
                        
#         return dp[m-1][n-1]
        