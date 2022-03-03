from itertools import groupby
# Time Complexity O(n) 48 ms
# Space Complexity O(n) 14.1 MB
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        
        diffs = []
        for idx, num in enumerate(nums[1:], 1):
            diffs.append(num - nums[idx - 1])
            
        result = 0
        for _, ns in groupby(diffs):
            sub_len = len(list(ns))
            result += sub_len * (sub_len - 1) // 2
        
        return result
    
# Time Complexity O(n) 53 ms
# Space Complexity O(1) 14.1 MB    
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        
        result, start, diff = 0, 0, nums[1] - nums[0]
        for idx, num in enumerate(nums[1:], 1):
            if num - nums[idx-1] != diff:
                sub_len = idx - start
                result += (sub_len - 2) * (sub_len - 1) // 2
                start = idx - 1
                diff = num - nums[idx-1]
                
        sub_len = len(nums) - start
        result += (sub_len - 2) * (sub_len - 1) // 2
        
        return result
    
# Time Complexity O(n) 58 ms
# Space Complexity O(1) 14.1 MB  
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        le=len(nums)
        l=[0]*(le)
        for i in range(2,le):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                l[i]=1+l[i-1]
        return sum(l)