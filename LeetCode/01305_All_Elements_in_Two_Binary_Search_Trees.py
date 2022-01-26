# Time Complexity O(n log n) 320 ms
# Space Complexity O(n) 22.9 MB
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:        
        def treeTraverse(node: TreeNode, cur_list: List[int]):
            if not node: 
                return
            treeTraverse(node.left, cur_list)
            cur_list.append(node.val)
            treeTraverse(node.right, cur_list)
        
        list1, list2 = [], []
        treeTraverse(root1, list1)
        treeTraverse(root2, list2)
        return sorted([*list1, *list2])

# Time Complexity O(n log n) 410 ms
# Space Complexity O(n) 23.1 MB
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:        
        def treeTraverse(node: TreeNode, cur_list: List[int]):
            if not node: 
                return
            treeTraverse(node.left, cur_list)
            cur_list.append(node.val)
            treeTraverse(node.right, cur_list)
        
        list1, list2 = [], []
        treeTraverse(root1, list1)
        treeTraverse(root2, list2)
        
        ans = []
        
        while list1 and list2:
            ans.append(list1.pop(0) if list1[0] < list2[0] else list2.pop(0))
        
        return ans + list1 + list2
            
        


# Time Complexity O(n) 5232 ms
# Space Complexity O(1) 24.5 MB
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:        
        def treeIter(node: TreeNode):
            if node:   
                yield from treeIter(node.left)
                yield node.val
                yield from treeIter(node.right)
                    
        r1i, r2i = treeIter(root1), treeIter(root2)
        
        try:
            r1 = next(r1i)
        except StopIteration as e:
            r1 = None
            
        try:
            r2 = next(r2i)
        except StopIteration as e:
            r2 = None
        
        result = []
       
        while (r1 is not None) and (r2 is not None):
            if r1 < r2:
                result.append(r1)
                try:
                    r1 = next(r1i)
                except StopIteration as e:
                    r1 = None
            else:
                result.append(r2)
                try:
                    r2 = next(r2i)
                except StopIteration as e:
                    r2 = None
        
        if r1 is not None:
            while r1 is not None:
                result.append(r1)
                try:
                    r1 = next(r1i)
                except StopIteration as e:
                    r1 = None
        elif r2 is not None:
            while r2 is not None:
                result.append(r2)
                try:
                    r2 = next(r2i)
                except StopIteration as e:
                    r2 = None
                
        return result
        
        