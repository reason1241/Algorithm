# Time Complexity O(n) 36 ms
# Space Complexity O(n) 15.2 MB
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        current = [(root, 1)]
        max_depth = 1
        while current:
            cur_node, cur_depth = current.pop(0)
            if cur_node.left: current.append((cur_node.left, cur_depth + 1))
            if cur_node.right: current.append((cur_node.right, cur_depth + 1))
            max_depth = max(max_depth, cur_depth)
        return max_depth
    
# Time Complexity O(n) 60 ms
# Space Complexity O(n) 16.4 MB    
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1