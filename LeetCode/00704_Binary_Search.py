# Time Complexity O(log n) 375 ms
# Space Complexity O(1) 15.3 MB
# binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        
        while left < right:
            mid = (left + right) // 2
                        
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left if left < len(nums) and nums[left] == target else -1

# # Time Complexity O(log n) 340 ms
# # Space Complexity O(1) 15.4 MB                
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
        
#         while left <= right:
#             mid = (left + right) // 2
                        
#             if nums[mid] == target: return mid
            
#             if nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         return -1
                
        