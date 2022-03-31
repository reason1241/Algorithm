# Time Complexity O(n) 952 ms
# Space Complexity O(n) 68.1 MB
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            if num > 0:
                nums_set.add(num)
                
        for i in range(1, 2**31):
            if i not in nums_set:
                return i
        return -1
    
# # Time Complexity O(n) 928 ms
# # Space Complexity O(1) 59.6 MB
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:        
#         for i in range(len(nums)):
#             while 0 < nums[i] <= len(nums):
#                 if nums[i] == nums[nums[i] - 1] or nums[i] == i + 1: break
#                 tmp = nums[i] - 1
#                 nums[i], nums[tmp] = nums[tmp], nums[i]
                
#         for i in range(len(nums)):
#             if nums[i] != i + 1: return i + 1
        
#         return len(nums) + 1
            
                