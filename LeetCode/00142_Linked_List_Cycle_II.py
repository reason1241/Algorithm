from typing import Optional

# Time Complexity O(n) 56 ms
# Space Complexity O(1) 17.5 MB 
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head:
            if type(head.val) is str:
                return head
            head.val = str(head.val)
            head = head.next
        return None

# Time Complexity O(n) 48 ms
# Space Complexity O(1) 17.3 MB
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:
            return None
        
        while head != slow:
            head = head.next
            slow = slow.next
        
        return head