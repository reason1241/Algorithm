# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity O(n) 61 ms
# Space Complexity O(n) 14.9 MB
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q, widths = [(root, 0)], []
        while q:
            widths.append(q[-1][1] - q[0][1] + 1)
            next_q = []
            for n, pos in q:
                if n:
                    if n.left:
                        next_q.append((n.left, pos * 2))
                    if n.right:
                        next_q.append((n.right, pos * 2 + 1))
            q = next_q
        return max(widths)
    
# from collections import defaultdict
# Time Complexity O(n) 112 ms
# Space Complexity O(n) 18.6 MB
# class Solution:
#     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         level_map = defaultdict(list)
        
#         def dfs(node, cur_level, pos):
#             if not node: return
            
#             dfs(node.left, cur_level + 1, pos * 2)
#             dfs(node.right, cur_level + 1, pos * 2 + 1)
            
#             level_map[cur_level].append(pos)
            
#         dfs(root, 0, 0)
        
#         max_width = 0
        
#         for _, v in level_map.items():
#             max_width = max(max_width, max(v) - min(v) + 1)
        
#         return max_width