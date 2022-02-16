# Time Complexity O(n) 43 ms
# Space Complexity O(1) 13.8 MB
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        bef = start = ListNode(-1, head)
        cur = bef.next
        while cur and cur.next:
            n = cur.next
            nn = cur.next.next
            cur.next = nn
            n.next = cur
            bef.next = n
            bef = cur
            cur = nn
        return start.next
    
# # Time Complexity O(n) 28 ms
# # Space Complexity O(1) 14 MB    
# # for readablilty
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         v = bef = ListNode(-1, head)
#         while head and head.next:
#             a = head
#             b = head.next
#             c = head.next.next
            
#             bef.next = b
#             bef.next.next = a
#             bef.next.next.next = c
            
#             bef = a
#             head = c
            
#         return v.next
    
# # Time Complexity O(n) 41 ms
# # Space Complexity O(1) 13.8 MB    
# # recursive
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head and head.next:
#             a = head
#             b = head.next
#             c = head.next.next
            
#             head = b
#             head.next = a
#             head.next.next = self.swapPairs(c)
        
#         return head

# # Time Complexity O(n) 48 ms
# # Space Complexity O(1) 14 MB        
# # recursive, reduce variables
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head and head.next:
#             tmp = head.next
#             head.next = self.swapPairs(tmp.next)
#             tmp.next = head
            
#             return tmp
        
#         return head