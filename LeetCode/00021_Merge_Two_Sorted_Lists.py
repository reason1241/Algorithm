# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity O(n) 39 ms
# Space Complexity O(1) 13.8 MB
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = ListNode(-1)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return head.next
    
    
# # Time Complexity O(n) 42 ms
# # Space Complexity O(1) 13.8 MB
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         head = cur = ListNode(-1)
#         while list1 and list2:
#             if list1.val < list2.val:
#                 cur.next = list1
#                 list1 = list1.next
#             else:
#                 cur.next = list2
#                 list2 = list2.next
#             cur = cur.next
        
#         cur.next = list1 or list2
#         return head.next
    
    
# # Time Complexity O(n) 36 ms
# # Space Complexity O(1) 14 MB
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if not (list1 and list2):
#             return list1 or list2
#         if list1.val < list2.val:
#             list1.next = self.mergeTwoLists(list1.next, list2)
#             return list1
#         else:
#             list2.next = self.mergeTwoLists(list1, list2.next)
#             return list2
        
        
# # Time Complexity O(n) 32 ms
# # Space Complexity O(1) 13.9 MB
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if not (list1 and list2):
#             return list1 or list2
#         if list1.val > list2.val:
#             list1, list2 = list2, list1
        
#         list1.next = self.mergeTwoLists(list1.next, list2)
#         return list1