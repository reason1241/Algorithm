# Time Complexity O(n) 56 ms
# Space Complexity O(1) 13.8 MB
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, twice = 0, False
        for fast, v in enumerate(nums[1:], 1):
            if nums[slow] == v:
                if twice:
                    continue
                twice = True
            else:
                twice = False
            nums[slow + 1] = v
            slow += 1
        return slow + 1

# Time Complexity O(n) 67 ms
# Space Complexity O(1) 13.8 MB   
# class Solution:
#     def removeDuplicates(self, nums):
#         i = 0
#         for n in nums:
#             if i < 2 or n > nums[i-2]:
#                 nums[i] = n
#                 i += 1
#         return i