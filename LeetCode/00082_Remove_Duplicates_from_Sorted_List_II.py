# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity O(n) 44 ms
# Space Complexity O(1) 14 MB
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:          
        dummyHead = conn = ListNode(-float('inf'))
        slow = fast = head
        
        while fast and fast.next:
            while fast and slow.val == fast.val:
                fast = fast.next
                      
            if slow.next == fast:
                slow.next = None
                conn.next = slow
                conn = conn.next
                
            slow = fast
            
        if slow == fast:
            conn.next = slow
            
        return dummyHead.next
    
# # Time Complexity O(n) 44 ms
# # Space Complexity O(1) 13.8 MB    
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:          
#         dummyHead = pre = ListNode(None, head)
        
#         while head:
#             if head.next and head.val == head.next.val:
#                 while head.next and head.val == head.next.val:
#                     head = head.next
#                 pre.next = head.next
#             else:
#                 pre = pre.next
#             head = head.next
#         return dummyHead.next