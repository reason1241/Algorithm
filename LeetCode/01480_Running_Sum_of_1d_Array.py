# Time Complexity O(n) 67 ms
# Space Complexity O(1) 14.1 MB
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result, cur = [], 0
        for num in nums:
            cur += num
            result.append(cur)
        return result
    
# # Time Complexity O(n) 64 ms
# # Space Complexity O(1)) 14.1 MB    
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         return [total := nums[0]] + [total := num + total for num in nums[1:]]