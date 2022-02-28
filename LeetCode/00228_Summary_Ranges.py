# Time Complexity O(n) 32 ms
# Space Complexity O(n) 13.9 MB
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return
        
        result = []
        
        start = 0
        
        for i, v in enumerate(nums[1:], 1):
            if nums[i-1] + 1 != v:
                if i == start + 1:
                    result.append(f"{nums[i-1]}")
                else:
                    result.append(f"{nums[start]}->{nums[i-1]}")
                start = i
        if start != len(nums) - 1:
            result.append(f"{nums[start]}->{nums[len(nums) - 1]}")
        else:
            result.append(f"{nums[start]}")
                
        return result