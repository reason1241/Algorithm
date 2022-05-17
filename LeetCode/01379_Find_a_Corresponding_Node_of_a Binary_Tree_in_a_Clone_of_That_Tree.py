# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Time Complexity O(n) 972 ms
# Space Complexity O(1) 23.8 MB
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def inOrder(node: TreeNode):
            if node:
                yield from inOrder(node.left)
                yield node
                yield from inOrder(node.right)
        
        o = inOrder(original)
        
        cnt = 0
        for on in o:
            if on == target:
                break
            cnt += 1
         
        c = inOrder(cloned)
        for _ in range(cnt):
            next(c)
              
        return next(c)
    
# # Time Complexity O(n) 800 ms
# # Space Complexity O(n) 24.2 MB
# class Solution:
#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         if not original:
#             return None
#         if original == target:
#             return cloned
        
#         return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)
            