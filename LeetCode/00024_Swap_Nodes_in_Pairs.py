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