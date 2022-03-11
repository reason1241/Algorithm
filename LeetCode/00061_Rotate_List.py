# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity O(n) 69 ms
# Space Complexity O(1) 13.8 MB
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        
        tail, length = head, 1
        
        while tail and tail.next:
            length+= 1
            tail = tail.next
        
        tail.next = head
        
        for _ in range(length  - (k % length)):
            head = head.next
            tail = tail.next
        
        tail.next = None
        return head 
    
# Time Complexity O(n) 24 ms
# Space Complexity O(1) 14 MB    
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        
        tail, length = head, 1
        
        while tail and tail.next:
            length+= 1
            tail = tail.next
        
        tail.next = head
        
        for _ in range(length  - (k % length) - 1):
            head = head.next
        
        tail = head
        head = head.next
        tail.next = None
        
        return head 