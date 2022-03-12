"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Time Complexity O(n) 32 ms
# Space Complexity O(n) 15 MB
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        
        node_map = {}
        cur = head
        while cur:
            if cur in node_map:
                new_cur = node_map[cur]
            else:
                new_cur = Node(cur.val)
                node_map[cur] = new_cur
            
            if cur.next:
                if cur.next in node_map:
                    new_next = node_map[cur.next]
                else:
                    new_next = Node(cur.next.val)
                    node_map[cur.next] = new_next
                new_cur.next = new_next
                
            if cur.random:
                if cur.random in node_map:
                    new_rand = node_map[cur.random]
                else:
                    new_rand = Node(cur.random.val)
                    node_map[cur.random] = new_rand
                new_cur.random = new_rand
                
            cur = cur.next
        
        return node_map[head]

# # Time Complexity O(n) 42 ms
# # Space Complexity O(n) 14.8 MB            
# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         if not head: return head
        
#         node_map = {}
#         cur = head
#         while cur:
#             if cur not in node_map:
#                 node_map[cur] = Node(cur.val)
            
#             if cur.next:
#                 if cur.next not in node_map:
#                     node_map[cur.next] = Node(cur.next.val)
#                 node_map[cur].next = node_map[cur.next]
                
#             if cur.random:
#                 if cur.random not in node_map:
#                     node_map[cur.random] = Node(cur.random.val)
#                 node_map[cur].random = node_map[cur.random]
                
#             cur = cur.next
        
#         return node_map[head]


# # Time Complexity O(n) 63 ms
# # Space Complexity O(n) 14.8 MB 
# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         if not head: return head
        
#         node_map, cur = {}, head
#         while cur:
#             node_map[cur] = Node(cur.val)
#             cur = cur.next
            
#         cur = head
#         while cur:
#             if cur.next:
#                 node_map[cur].next = node_map[cur.next]
#             if cur.random:
#                 node_map[cur].random = node_map[cur.random]
#             cur = cur.next
        
#         return node_map[head]

# # Time Complexity O(n) 66 ms
# # Space Complexity O(n) 14.9 MB 
# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':       
#         cur = head
#         while cur:
#             cur_copy = Node(cur.val, cur.next, None)
#             cur.next = cur_copy
#             cur = cur.next.next
        
#         cur = head
#         clone_head = clone_cur = Node(-1)
#         while cur:
#             if cur.random:
#                 cur.next.random = cur.random.next
#             clone_cur.next = cur.next
#             clone_cur = clone_cur.next
#             cur = cur.next.next
        
#         return clone_head.next
            
# # Time Complexity 92 ms
# # Space Complexity 18.2 MB
# import copy
# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         return copy.deepcopy(head)
    
