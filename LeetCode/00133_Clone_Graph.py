"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Time Complexity O(n) 36 ms
# Space Complexity O(n) 14.5 MB
# dfs
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return 
        
        visited = {}
        
        def _cloneGraph(node):
            visited[node] = cur_node = Node(node.val)
            
            for next_node in node.neighbors:
                if next_node in visited:
                    cur_node.neighbors.append(visited[next_node])
                    continue
                cur_node.neighbors.append(visited[_cloneGraph(next_node)])
                    
            return node
                    
        return visited[_cloneGraph(node)]

# # Time Complexity O(n) 52 ms
# # Space Complexity O(n) 14.4 MB
# dfs
# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if not node: return
        
#         visited = {node: Node(node.val)}
#         stack = [node]
        
#         while stack:
#             current = stack.pop()
            
#             for next_node in current.neighbors:
#                 if next_node not in visited:
#                     stack.append(next_node)
#                     visited[next_node] = Node(next_node.val)
#                 visited[current].neighbors.append(visited[next_node])
#         return visited[node]
                
# # Time Complexity O(n) 61 ms
# # Space Complexity O(n) 14.4 MB  
# bfs        
# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if not node: return
        
#         visited = {node: Node(node.val)}
#         q = [node]
        
#         while q:
#             current = q.pop(0)
            
#             for next_node in current.neighbors:
#                 if next_node not in visited:
#                     visited[next_node] = Node(next_node.val)
#                     q.append(next_node)  
#                 visited[current].neighbors.append(visited[next_node])
#         return visited[node]            
            


# import copy
# # Time Complexity O(n) 51 ms
# # Space Complexity O(n) 14.7 MB
# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':        
#         return copy.deepcopy(node)