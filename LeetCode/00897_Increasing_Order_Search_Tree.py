# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity O(log n + k) 56 ms
# Space Complexity O(log n + k) 17.9 MB
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(node: Optional[TreeNode]):
            if node:
                yield from inOrder(node.left)
                yield node.val
                yield from inOrder(node.right)
    
        gen = inOrder(root)
        for _ in range(k-1):
            next(gen)
        
        return next(gen)
    
# # Time Complexity O(log n + k) 51 ms
# # Space Complexity O(log n) 17.9 MB
# Memorize!
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         stack = []
        
#         while True:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             k -= 1
#             if not k: return root.val
#             root = root.right