# Time Complexity O(n!) 48 ms
# Space Complexity O(n!) 14.5 MB
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def recursivePermute(nums: List[int], selected: List[int]):
            if not nums: 
                result.append(selected)
                return
            
            for idx, num in enumerate(nums):
                if num in nums[:idx]:
                    continue
                recursivePermute(nums[:idx] + nums[idx+1:], selected+[num])
                
        recursivePermute(nums, [])
        return result
                    