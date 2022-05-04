from collections import Counter

# Time Complexity O(n) 812 ms
# Space Complexity O(n) 27.1 MB
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        result = 0
        for i in c:
            if k - i in c:
                if k - i == i:
                    diff = c[i] // 2
                else:
                    diff = min(c[i], c[k - i])
                result += diff
                c[i] -= diff
                c[k - i] -= diff
        return result
    
    
# from collections import Counter
# # Time Complexity O(n) 651 ms
# # Space Complexity O(n) 27 MB
# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         c = Counter(nums)
#         result = 0
#         for i in c:
#             if k - i > 0 and k - i in c:
#                 if k - i == i:
#                     diff = c[i] // 2
#                 else:
#                     diff = min(c[i], c[k - i])
#                 result += diff
#                 c[i] -= diff
#                 c[k - i] -= diff
#         return result
    
# from collections import Counter
# # Time Complexity O(n) 813 ms
# # Space Complexity O(n) 27.3 MB
# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         c = Counter(nums)
#         result = 0
#         for i in c:
#             if i <= k - i and k - i in c:
#                 if k - i == i:
#                     diff = c[i] // 2
#                 else:
#                     diff = min(c[i], c[k - i])
#                 result += diff
#         return result
    

# # Time Complexity O(n log n) 966 ms
# # Space Complexity O(1) 26.2 MB    
# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         nums.sort()
        
#         f, b = 0, len(nums) - 1
#         result = 0
        
#         while f < b:
#             if nums[f] + nums[b] == k:
#                 result += 1
#                 f += 1
#                 b -= 1
#             elif nums[f] + nums[b] < k:
#                 f += 1
#             else:
#                 b -= 1
        
#         return result