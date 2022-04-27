from collections import defaultdict

# Time Complexity O(p + n log n) 1224 ms
# Space Complexity O(n) 50.5 MB
# union find
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        roots = [i for i in range(len(s))]
        ranks = [1] * len(s)
        
        def find(pos: int) -> int:
            if roots[pos] == pos: return pos
            roots[pos] = find(roots[pos])
            return roots[pos]
        
        def union(pos1: int, pos2: int):
            root1, root2 = find(pos1), find(pos2)
            
            if root1 == root2: return
            
            if ranks[root1] < ranks[root2]: 
                roots[root1] = root2
            else: 
                roots[root2] = root1
                
        for pair in pairs:
            union(pair[0], pair[1])
        
        pos_dict = defaultdict(list)
        for i in range(len(s)):
            pos_dict[find(i)].append(s[i])
        
        for l in pos_dict.values():
            l.sort()
            
        result = ""
        
        for root in roots:
            result += f"{pos_dict[root].pop(0)}"
            
        return result
            
            
            
# from collections import defaultdict
# # Time Complexity O(p + n log n) 1224 ms
# # Space Complexity O(n) 50.5 MB
# # dfs
# # Using an array for visited is far faster than using a set
# # For m, using a defaultdict is slower than the current implementation
# class Solution:
#     def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
#         m = [[] for _ in range(len(s))]
        
#         for pair in pairs:
#             m[pair[0]].append(pair[1])
#             m[pair[1]].append(pair[0])
            
#         visited = [False] * len(s)
#         ps = list(range(len(s)))
#         root_m = defaultdict(list)
        
#         for i in range(len(s)):
#             if visited[i]: 
#                 continue
            
#             stk = [i]
#             visited[i] = True
            
#             while stk:
#                 cur = stk.pop()
#                 ps[cur] = i
#                 root_m[i].append(s[cur])
                
#                 for n in m[cur]:
#                     if not visited[n]:
#                         stk.append(n)
#                         visited[n] = True
                        
#             root_m[i].sort(reverse=True)
        
#         l = []
#         for i in range(len(ps)):
#             l.append(root_m[ps[i]].pop())
        
#         return "".join(l)
            
            