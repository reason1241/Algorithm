# Time Complexity O(n**2) Time Limit Exceeded
# Space Complexity O(1)
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                max_xor = max(max_xor, nums[i] ^ nums[j])
                
        return max_xor
    
    
# Time Complexity O(n log n) 432 ms faster than 99.66%
# Space Complexity O(n) 33.5 MB beats 97.55%
# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         if len(nums) < 10:
#             max_val = 0
#             for i in range(len(nums)):
#                 for j in range(i+1, len(nums)):
#                     max_val = max(max_val, nums[i] ^ nums[j])
#             return max_val
        
#         nums = sorted(nums)
#         checker = set(nums)
        
#         upper_bound = 1
#         while upper_bound < nums[-1]:
#             upper_bound <<= 1
#         lower_bound = upper_bound >> 1
#         upper_bound -= 1
        
#         lower_pos = len(nums) - 1
#         while nums[lower_pos] > lower_bound:
#             lower_pos -= 1
        
#         predict = upper_bound
        
#         while predict > 0:
#             for i in range(len(nums)-1, lower_pos - 1, -1):
#                 target_val = predict ^ nums[i]
#                 if target_val in checker:
#                     return predict
#             predict -= 1
#         return 0

# if val1 ^ val2 = ans => ans ^ val2 = val1 ^ val2 ^ val2 => ams ^ val2 = val1
# Time Complexity O(n) 788 ms
# Space Complexity O(n) 33.5 MB
# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         ans, mask = 0, 0
#         max_len = len(bin(max(nums))[2:])
        
#         for i in range(max_len, -1, -1):
#             mask |= 1 << i
#             prefixes = { mask & num for num in nums }
#             temp_ans = ans | (1 << i)
#             if any(temp_ans ^ prefix in prefixes for prefix in prefixes):
#                 ans = temp_ans
#         return ans