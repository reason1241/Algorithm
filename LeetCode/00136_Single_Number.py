from collections import Counter
# Time Complexity O(n) 171 ms
# Space Complexity O(n) 16.6 MB	
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for i, v in c.items(): 
            if v != 2: return i
            
from collections import Counter
# Time Complexity O(n) 242 ms
# Space Complexity O(1) 16.7 MB	
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
            