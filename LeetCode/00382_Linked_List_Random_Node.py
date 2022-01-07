import random

# Time Complexity initialize O(n), getRandom O(1) 99 ms
# Space Complexity O(n) 17.4 MB
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.all_num_list = []
        while head:
            self.all_num_list.append(head.val)
            head = head.next
        self.num_len = len(self.all_num_list)
        

    def getRandom(self) -> int:
        picked = random.randint(0, self.num_len - 1)
        return self.all_num_list[picked]
    
    

# Reservoir Sampling 
# This problem focuses on the Space Complexity
# Time Complexity initialize O(1), getRandom O(n) 253 ms
# Space Complexity O(1) 17.3 MB
# import random

# class Solution:

#     def __init__(self, head: Optional[ListNode]):
#         self.head = head
        

#     def getRandom(self) -> int:
#         current, total = self.head, 0
#         result = current.val
        
#         while current:
#             if random.randint(0, total) == 0:
#                 result = current.val
#             current = current.next
#             total += 1
        
#         return result

