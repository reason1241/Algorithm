from collections import Counter
# Time Complexity O(n) 172 ms
# Space Complexity (n) 15.5 MB
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        for i, v in c.items():
            if v >= ceil(len(nums)/2):
                return i
            
# Time Complexity O(n) 292 ms
# Space Complexity (1) 15.6 MB       
# Boyer-Moore Voting Algorithm    
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj, cnt = 0, 0
        for num in nums:
            if cnt == 0:
                maj = num
            cnt += (1 if num == maj else -1)
        return maj
    
        
# Time Complexity O(n) 177 ms
# Space Complexity (1) 15.4 MB       
# random    
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate
        
