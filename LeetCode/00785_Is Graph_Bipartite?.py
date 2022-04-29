# Time Complexity O(v + e) 226 ms
# Spce Complexity O(v) 14.8 MB
# dfs
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        groups = [set(), set()]
        
        def dfs(cur_point: int, cur_group: int):
            if cur_point in groups[cur_group ^ 1]:
                return False
            elif cur_point in groups[cur_group]:
                return True
            
            groups[cur_group].add(cur_point)
            
            result = True
            
            for next_vertex in graph[cur_point]:
                result &= dfs(next_vertex, cur_group ^ 1)
            
            return result
            
        for vertex in range(len(graph)):
            if vertex in groups[0] or vertex in groups[1]:
                continue
            
            if not dfs(vertex, 0):
                return False
        
        return True

# # Time Complexity O(v + e) 193 ms
# # Spce Complexity O(v) 14.3 MB
# # bfs
# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         colors = {}
        
#         for v in range(len(graph)):
#             if v not in colors:
#                 q = [v]
#                 colors[v] = 0
                
#                 while q:
#                     cur_v = q.pop(0)
#                     for adj in graph[cur_v]:
#                         if adj not in colors:
#                             colors[adj] = colors[cur_v] ^ 1
#                             q.append(adj)
#                         else:
#                             if colors[adj] == colors[cur_v]:
#                                 return False
                            
#         return True
                    