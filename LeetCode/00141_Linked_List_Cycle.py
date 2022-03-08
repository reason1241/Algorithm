# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time Complexity O(n) 56 ms
# Space Complexity O(n) 17.9 MB
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False
    
# # Time Complexity O(n) 66 ms
# # Space Complexity O(1) 17.5 MB    
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         slow = fast = head
        
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
        
#         return False