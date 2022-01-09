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