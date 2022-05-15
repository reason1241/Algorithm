# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity O(n) 241 ms
# Space Complexity O(n) 17.8 MB
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        
        result = 0
        
        while q:
            cur_sum = 0
            for _ in range(len(q)):
                cur = q.pop(0)
                cur_sum += cur.val        
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            result = cur_sum
        
        return result
    
# # Time Complexity O(n) 219 ms
# # Space Complexity O(n) 17.8 MB    
# class Solution:
#     def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
#         pre,cur=[],[root]
#         while cur:
#             pre,cur=cur,[child for node in cur for child in [node.left,node.right] if child]
#         return sum(node.val for node in pre)
                
        