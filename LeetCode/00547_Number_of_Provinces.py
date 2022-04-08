# Time Complexity O(n ** 2) 237 ms
# Space Complexity O(n) 14.8 MB
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        
        def dfs(current_city: int):
            if current_city in visited:
                return
            
            visited.add(current_city)
            
            for i, v in enumerate(isConnected[current_city]):
                if v:
                    dfs(i)
            return
        
        result = 0
        
        for city in range(len(isConnected)):
            if city in visited:
                continue
                
            dfs(city)
            result += 1
            
        return result
    
    
    
# # Time Complexity O(n ** 2) 176 ms
# # Space Complexity O(n) 14.2 MB    
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         stack = []
#         not_visited = set(range(len(isConnected)))
#         result = 0
        
#         while not_visited:
#             city = stack.pop() if stack else not_visited.pop()
            
#             for i in range(len(isConnected[city])):
#                 if isConnected[city][i] and i in not_visited:
#                     not_visited.remove(i)
#                     stack.append(i)
                    
#             if not stack or not not_visited:
#                 result += 1
        
#         return result
            
            