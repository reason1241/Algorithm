from collections import defaultdict

# Time Complexity O(n) 364 ms
# Space Complexity O(n) 16.6 MB
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d, cur, result = defaultdict(int), 0, 0
        d[0] = 1
        for num in nums:
            cur += num
            if cur - k in d:
                result += d[cur - k]
            d[cur] += 1
        return result
        

# # Time Complexity O(n) 407 ms
# # Space Complexity O(n) 16.5 MB
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         d, cur, result = {0:1}, 0, 0
#         for num in nums:
#             cur += num
#             result += d.get(cur-k, 0)
#             d[cur] = d.get(cur, 0) + 1
#         return result
        
        