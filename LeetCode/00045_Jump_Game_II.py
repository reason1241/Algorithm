from collections import deque
# Time Complexity O(n) 15299 ms
# Space Complexity O(n) 68.6 MB
class Solution:
    def jump(self, nums: List[int]) -> int:
        q, visited = deque([(0, 0)]), set()
        while q:
            cur_idx, steps = q.popleft()
            if cur_idx == len(nums) - 1: return steps
            if cur_idx in visited: continue
            visited.add(cur_idx)
            for i in range(1, nums[cur_idx] + 1):
                q.append((cur_idx + i, steps + 1))
        return -1
    
    
# from collections import deque
# # Time Complexity O(n) 7244 ms
# # Space Complexity O(n) 15.3 MB
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         q, visit_max = deque([(0, 0)]), 1
#         while q:
#             cur_idx, steps = q.popleft()
#             if cur_idx == len(nums) - 1: return steps
#             for i in range(visit_max, cur_idx + nums[cur_idx] + 1):
#                 q.append((i, steps + 1))
#             if cur_idx + nums[cur_idx] > visit_max:
#                 visit_max = cur_idx + nums[cur_idx]
#         return -1

# # Time Complexity O(n) 211 ms
# # Space Complexity O(1) 14.9 MB
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         if len(nums) == 1: return 0
#         cur_end, cur_farthest, jumps = nums[0], nums[0], 0
#         for i, v in enumerate(nums[1:-1], 1):
#             cur_farthest = max(cur_farthest, i + v)
#             if cur_end == i:
#                 jumps += 1
#                 cur_end = cur_farthest
#         return jumps + 1

# # Time Complexity O(n) 181 ms
# # Space Complexity O(1) 15 MB    
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         cur_end, cur_farthest, jumps = 0, 0, 0
#         for i, v in enumerate(nums[:-1]):
#             cur_farthest = max(cur_farthest, i + v)
#             if cur_end == i:
#                 jumps += 1
#                 cur_end = cur_farthest
#         return jumps
        
# # Time Complexity O(n) 230 ms
# # Space Complexity O(1) 15 MB              
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         cur_end, cur_farthest, jumps = 0, 0, 0
#         for i, v in enumerate(nums[:-1]):
#             cur_farthest = max(cur_farthest, i + v)
#             if cur_end == i:
#                 jumps += 1
#                 cur_end = cur_farthest
#                 if cur_farthest >= len(nums) - 1: break
#         return jumps
        
            
            