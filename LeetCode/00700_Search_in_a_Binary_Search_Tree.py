# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity O(log n) 79 ms
# Space Complexity O(log n) 16.4 MB	because of the recursion
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def bs(root: Optional[TreeNode]) ->Optional[TreeNode]:
            if not root: return None
            if root.val == val: return root
            
            if root.val > val: return bs(root.left)
            return bs(root.right)
        
        return bs(root)
    
# # Time Complexity O(log n) 86 ms
# # Space Complexity O(1) 16.4 MB	    
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if not root or root.val == val: return root
#         return self.searchBST(root.left, val) if root.val > val else self.searchBST(root.right, val)
    
    
# # Time Complexity O(log n) 74 ms
# # Space Complexity O(1) 16.4 MB	  
# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         while root and root.val != val:
#             root = root.left if root.val > val else root.right
#         return root
    