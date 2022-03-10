# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity O(n) 77 ms
# Space Complexity O(n) 14.1 MB	
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fore = head = ListNode(None)
        
        carry = 0
        
        while l1 or l2:
            temp = 0
            if l1:
                temp += l1.val
                l1 = l1.next
            
            if l2:
                temp += l2.val
                l2 = l2.next
            
            if carry:
                temp += 1
                carry = 0
            
            if temp >= 10:
                temp -= 10
                carry = 1
                
            head.next = ListNode(temp)
            head = head.next
        
        if carry:
            head.next = ListNode(carry)
        
        return fore.next

# Time Complexity O(n) 98 ms
# Space Complexity O(n) 13.9 MB	
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fore = head = ListNode(None)
        
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            
            if l2:
                carry += l2.val
                l2 = l2.next
            
            head.next = ListNode(carry % 10)
            carry //= 10
            head = head.next
        
        return fore.next