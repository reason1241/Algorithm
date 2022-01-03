# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# compare n in k times
# time complexity : O(kn), 6916 ms	
# space complexity : O(n), 17.6 MB
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:             
        head = ListNode(-1)
        current_node = head
                
        while True:
            min_idx = -1
            min_val = 9876            
            for idx in range(len(lists)):
                if lists[idx]:
                    if lists[idx].val< min_val:
                        min_idx = idx
                        min_val = lists[idx].val
            
            if min_idx < 0:
                break
                       
            current_node.next = lists[min_idx]
            lists[min_idx] = lists[min_idx].next
            current_node = current_node.next
        
        return head.next
    

# import heapq
# # use heap to compare values
# # time complexity : O(nlogn), 104 ms
# # space complexity : O(n), 18.3 MB
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:             
#         hq = []
               
#         for a_list in lists:
#             while a_list:
#                 heapq.heappush(hq, a_list.val)
#                 a_list = a_list.next
        
#         head = ListNode(-1)
#         current_node = head
        
#         while len(hq) > 0:
#             next_val = heapq.heappop(hq)
#             current_node.next = ListNode(next_val)
#             current_node = current_node.next
        
#         return head.next
                

# merge with divide and conquer
# time complexity : O(n logk), 116 ms
# space complexity : O(1), 17.8 MB

# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:             
#         def merge2Lists(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
#             head = current_node = ListNode(-1)
            
#             while a and b:
#                 if a.val > b.val:
#                     current_node.next = b
#                     b = b.next
#                 else:
#                     current_node.next = a
#                     a = a.next
#                 current_node = current_node.next
                    
#             if not a:
#                 current_node.next = b
#             elif not b:
#                 current_node.next = a
#             return head.next
        
#         mid_lists = lists
#         while len(mid_lists) > 1:
#             temp_lists = []
            
#             loop_val = (len(mid_lists) // 2) * 2
            
#             for i in range(0, loop_val, 2):
#                 temp_lists.append(merge2Lists(mid_lists[i], mid_lists[i+1]))
                
#             if len(mid_lists) % 2 == 1:
#                 temp_lists.append(mid_lists[-1])
            
#             mid_lists = temp_lists
        
#         return None if not mid_lists else mid_lists[0]
                