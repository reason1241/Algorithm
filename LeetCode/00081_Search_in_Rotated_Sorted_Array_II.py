# Time Complexity O(n) 68 ms
# Space Complexity O(1) 14.4 MB
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target: return True
            
            if nums[left] <= nums[mid]:
                if nums[left] == nums[mid] == nums[right]:
                    left += 1
                    continue
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
        
# # Time Complexity O(n) 60 ms
# # Space Complexity O(1) 14.3 MB    
# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
#         return target in nums

        