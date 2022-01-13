from typing import List

# Time Complexity O(nlogn) 2200 ms because of the sort
# Space Complexity O(n) 58.6 MB
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        # there are 4 cases from the sorted points
        # 1) A: [1, 3], B: [1, 5] => hit box is [1, 3]
        # 2) A: [1, 4], B: [2, 3] => hit box is [2, 3]
        # 3) A: [1, 3], B: [2, 4] => hit box is [2, 3]
        # 4) A: [1, 2], B: [3, 4] => No hit box
        
        arrows = 0
        hit_box = points[0]
        for point in points[1:]:              
            # case 4
            if hit_box[1] < point[0]:
                arrows += 1
                hit_box = point
                continue
            # case 1,2,3
            hit_box[0] = max(hit_box[0], point[0])
            hit_box[1] = min(hit_box[1], point[1])
        return arrows + 1            

# use heap
# Time Complexity O(nlogn) 1903 ms
# Space Complexity O(n) 49.4 MB
import heapq

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        heapq.heapify(points)
        arrows = 0
        hit_box = points[0]
        while points:
            point = heapq.heappop(points)
            # case 4
            if hit_box[1] < point[0]:
                arrows += 1
                hit_box = point
                continue
            # case 1,2,3
            hit_box[0] = max(hit_box[0], point[0])
            hit_box[1] = min(hit_box[1], point[1])
        return arrows + 1            
            
# sort with the last values
# 1276 ms, 59.1 MB
# class Solution:
#     def findMinArrowShots(self, points: List[List[int]]) -> int:
#         points.sort(key=lambda x: x[1])
#         arrows, last_pos = 0, points[0][1]
#         for first, last in points:
#             if last_pos < first:
#                 arrows += 1
#                 last_pos = last
#         return arrows + 1