# Time Complexity O(n) 516 ms
# Space Complexity O(n) 34.1 MB
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        
        roots, ranks = [i for i in range(n)], [1] * n
        
        def find(node: int) -> int:
            # find root
            if roots[node] == node:
                return node            
            return find(roots[node])

        
        def union(node1: int, node2: int):
            n1r, n2r = find(node1), find(node2)
            
            # The root is same
            if n1r == n2r: return
            
            # Roots are different
            if ranks[n1r] < ranks[n2r]:
                # The node1Root will be under the node2Root
                roots[n1r] = n2r
                ranks[n2r] += 1
                ranks[n1r] = 1
            else:
                roots[n2r] = n1r
                ranks[n1r] += 1
                ranks[n2r] = 1
        
        for conn in connections:
            union(conn[0], conn[1])
            
        for node in range(n):
            roots[node] = find(node)
            
        return len(set(roots)) - 1
        
        
# # Time Complexity O(n) 802 ms
# # Space Complexity O(n) 33.9 MB
# class Solution:
#     def makeConnected(self, n: int, connections: List[List[int]]) -> int:
#         if len(connections) < n - 1: return -1
        
#         components, roots = n, [i for i in range(n)]
        
#         def find(node: int) -> int:
#             # find root
#             if roots[node] == node:
#                 return node           
#             roots[node] = find(roots[node])
#             return roots[node]

              
#         for conn in connections:
#             n1r, n2r = find(conn[0]), find(conn[1])
            
#             if n1r != n2r:
#                 roots[n2r] = n1r
#                 components -= 1
            
#         return components - 1
        
        