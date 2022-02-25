# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity O(n log n) 412 ms
# Space Complexity O(log n) 30 MB
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next): return head
        slow = fast = head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def merge(self, left: ListNode, right: ListNode):
        temp = cur = ListNode(-1)
        while left and right:
            if left.val > right.val:
                cur.next = right
                right = right.next
            else:
                cur.next = left
                left = left.next
            cur = cur.next
                        
        if left:
            cur.next = left
        elif right:
            cur.next = right
        return temp.next           

# Time Complexity O(n log n) 618 ms
# Space Complexity O(1) 30.1 MB
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head or not head.next: return head
        
#         list_len = self.listLength(head)
#         step = 1
        
#         forehead = ListNode(-1)
#         forehead.next = head
        
#         while step < list_len:
#             cur, tail = forehead.next, forehead
            
#             while cur:
#                 first = cur
#                 second = self.getNextPoint(first, step)
#                 next_point = self.getNextPoint(second, step)
                
#                 mhead, mtail = self.merge(first, second)
#                 # print(f"mhead: {mhead}")
#                 # print(f"mtail: {mtail}")
                
#                 tail.next = mhead
#                 tail = mtail
#                 cur = next_point
                
#             step *= 2
#         return forehead.next
        
        
#     def listLength(self, head: Optional[ListNode]) -> int:
#         cnt = 0
#         while head:
#             head = head.next
#             cnt += 1
#         return cnt
    
#     def merge(self, left: ListNode, right: ListNode):
#         tmp = cur = ListNode(-1)
#         while left and right:
#             if left.val > right.val:
#                 cur.next = right
#                 right = right.next
#             else:
#                 cur.next = left
#                 left = left.next
#             cur = cur.next
                        
#         if left:
#             cur.next = left
#         elif right:
#             cur.next = right
        
#         while cur and cur.next:
#             cur = cur.next
            
#         return (tmp.next, cur)
        
    
#     def getNextPoint(self, head: Optional[ListNode], step: int) -> Optional[ListNode]:
#         if not head: return None
        
#         while head and step > 1:
#             head = head.next
#             step -= 1
        
#         if not head:
#             return None
        
#         next_point = head.next
#         head.next = None
        
#         return next_point