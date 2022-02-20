# Time Complexity O(n log n) 121 ms
# Space Complexity O(1) 14.5 MB
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        result = len(intervals)
        c, d = intervals[0]
        for a, b in intervals[1:]:
            if c <= a and b <= d:
                result -= 1
                continue
            c, d = (a, b)
        return result
    
# # Time Complexity O(n log n) 132 ms
# # Space Complexity O(1) 14.5 MB        
# class Solution:
#     def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
#         d = result = 0
#         for _, b in sorted(intervals, key=lambda x: (x[0], -x[1])):
#             if b > d:
#                 result += 1
#                 d = b
#         return result
        