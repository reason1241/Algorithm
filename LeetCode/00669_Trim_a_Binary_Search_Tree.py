# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity O(n) 48 ms
# Space Complexity O(n) 18 MB
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root: return None
        
        if root.val > high:
            # all values are on the left side
            return self.trimBST(root.left, low, high)
        elif root.val < low:
            # all values are on the right side
            return self.trimBST(root.right, low, high)
        
        # all values are on the both side
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
