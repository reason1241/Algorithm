# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity O(n) 1072 ms
# Space Complexity O(1) 48.5 MB
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = fast = slow = ListNode(-1, head)
        
        for _ in range(k):
            fast = fast.next
        
        pivot = fast
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        pivot.val, slow.next.val = slow.next.val, pivot.val
        
        return dummy_head.next
        
# # Time Complexity O(n) 1422 ms
# # Space Complexity O(1) 48.7 MB
# class Solution:
#     def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         fast = slow = head
        
#         for _ in range(k - 1):
#             fast = fast.next
        
#         pivot = fast
        
#         while fast.next:
#             fast = fast.next
#             slow = slow.next
        
#         pivot.val, slow.val = slow.val, pivot.val
        
#         return head
        
        