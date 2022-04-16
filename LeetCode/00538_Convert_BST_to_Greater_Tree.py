# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity O(n) 98 ms
# Space Complexity O(n) 16.9 MB
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverseBST(root: Optional[TreeNode], cur_val: int) -> int:
            if not root: 
                return cur_val
            
            root.val += traverseBST(root.right, cur_val)            
            return traverseBST(root.left, root.val)
        
        traverseBST(root, 0)
        return root
        