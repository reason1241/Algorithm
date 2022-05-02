# Time Complexity O(n log n) 88 ms
# Space Complexity O(n) 14.7 MB
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x : x % 2)
    
    
# # Time Complexity O(n) 79 ms
# # Space Complexity O(n) 14.6 MB
# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         return [num for num in nums if not num % 2] + [num for num in nums if num % 2]
    
    
# # Time Complexity O(n) 79 ms
# # Space Complexity O(n) 14.7 MB    
# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         vs = [[],[]]
#         for num in nums:
#             vs[num % 2].append(num)
        
#         return vs[0] + vs[1]    
    
    
# # Time Complexity O(n) 143 ms
# # Space Complexity O(n) 14.5 MB    
# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         even, odd = 0, len(nums) - 1
        
#         while even < odd:
#             if nums[even] % 2 == 1 and nums[odd] % 2 == 0:
#                 nums[even], nums[odd] = nums[odd], nums[even]
#             if nums[even] % 2 == 0:
#                 even += 1
#             if nums[odd] % 2 == 1:
#                 odd -= 1
        
#         return nums