from collections import defaultdict

# Time Complexity O(n) 1301 ms
# Space Complexity O(n) 53 MB
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        company_map = defaultdict(list)
        for e, m in enumerate(manager):
            company_map[m].append(e)
        
        max_time = 0 
        
        def dfs(cur_node, cur_time):
            if informTime[cur_node] == 0:
                nonlocal max_time
                max_time = max(cur_time, max_time)
                return
            
            for subordinate in company_map[cur_node]:
                dfs(subordinate, cur_time + informTime[cur_node])
        
        dfs(headID, 0)
        
        return max_time
    
# # bottom up approach
# # Time Complexity O(n) 1193 ms
# # Space Complexity O(n) 40.5 MB    
# class Solution:
#     def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
#         def dfs(e: int) -> int:
#             if manager[e] != -1:
#                 informTime[e] += dfs(manager[e])
#                 manager[e] = -1
#             return informTime[e]
#         return max(map(dfs, range(n)))