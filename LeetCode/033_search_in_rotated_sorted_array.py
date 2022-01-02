# Tt mignt not be acceptable because the time complexity of this logic is O(n)
# But this logic was approved by leetcode
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         for idx, num in enumerate(nums):
#             if target == num:
#                 return idx
        
#         return -1

# Find pivot location and do binary search with the pivot
# time complexity : O(log n)
# space complexity : O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot(start_idx: int, end_idx: int) -> int:
            if end_idx - start_idx == 1:
                return start_idx if nums[start_idx] < nums[end_idx] else end_idx
            
            mid_idx = (start_idx + end_idx) // 2
            
            if nums[start_idx] > nums[mid_idx]:
                return findPivot(start_idx, mid_idx)
            elif nums[mid_idx] > nums[end_idx]:
                return findPivot(mid_idx, end_idx)
            return start_idx
        
        pivot_idx = findPivot(0, len(nums) - 1)

        def binarySearch(start_idx: int, end_idx: int) -> int:
            r_start_idx = (start_idx + pivot_idx) % len(nums)
            r_end_idx = (end_idx + pivot_idx) % len(nums)
            
            if start_idx == end_idx:
                if nums[r_start_idx] != target:
                    return -1
                
                return r_start_idx
            
            if abs(end_idx - start_idx) == 1:
                if nums[r_start_idx] == target:
                    return r_start_idx
                elif nums[r_end_idx] == target:
                    return r_end_idx
                else:
                    return -1
            
            mid_idx = (start_idx + end_idx) // 2
            r_mid_idx = (mid_idx + pivot_idx) % len(nums)

            if target>=nums[r_start_idx] and target<=nums[r_mid_idx]:
                return binarySearch(start_idx, mid_idx)
            elif target>=nums[r_mid_idx] and target<=nums[r_end_idx]:
                return binarySearch(mid_idx, end_idx)
            return -1
        
        return binarySearch(0, len(nums) - 1)
        
# don't find pivot location
# Time Comlexity O(log n)
# Space Complexity O(1)
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         lo, hi = 0, len(nums) - 1
        
#         while lo <= hi:
#             mid = (lo + hi) // 2

#             if nums[mid] == target:
#                 return mid
            
#             if nums[lo] <= nums[mid]:
#                 # forward part is in ascending order
#                 # or lo, mid has a pivot
#                 if nums[lo] <= target <= nums[mid]:
#                     hi = mid - 1
#                 else:
#                     lo = mid + 1
#             else:
#                 # backward part is in ascending order
#                 if nums[mid] <= target <= nums[hi]:
#                     lo = mid + 1
#                 else:
#                     hi = mid - 1

#         return -1