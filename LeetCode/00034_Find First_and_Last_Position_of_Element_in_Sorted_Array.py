from typing import List

# use binary search to find first and last
# Time Complexity O(log n) 87 ms
# Space Complexity O(1) 15.4 MB
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst() -> int:
            lo, hi = 0, len(nums) - 1

            while lo < hi:
                mid = (lo + hi) // 2

                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return hi if nums[hi] == target else -1

        def findLast() -> int:
            lo, hi = 0, len(nums) - 1
            while (hi - lo) > 1:
                mid = (lo + hi) // 2

                if nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid
            if nums[hi] == target:
                return hi
            elif nums[lo] == target:
                return lo
            return -1
        
        return [findFirst(), findLast()] if len(nums) > 0 else [-1, -1]
    
# use python library
# 88 ms
# 15.5 MB
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         left = bisect_left(nums, target)
#         if (left > len(nums) - 1) or (nums[left] != target): return [-1, -1]
#         return [left, bisect_right(nums, target) - 1]
    
# use just a binary search
# 76 ms
# 15.4 MB
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if len(nums) < 1: return [-1, -1]
        
#         def findFirst(target: int) -> int:
#             lo, hi = 0, len(nums)
#             while lo < hi:
#                 mid = (lo + hi) // 2
#                 if nums[mid] < target:
#                     lo = mid + 1
#                 else:
#                     hi = mid
#             return hi
        
#         lo, hi = findFirst(target), findFirst(target + 1) - 1
#         return [lo, hi] if lo <= hi else [-1, -1]