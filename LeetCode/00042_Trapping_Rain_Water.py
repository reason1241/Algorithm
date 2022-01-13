# Fill the box with water
# and cut it from the top
# but the max of n is 20,000
# the max of height is 100,000
# 2,000,000,000 will be fail to calculate

# dp
# Time Complexity O(n) 210 ms
# Space Complexity O(n) 15.6 MB
from typing import List

class Solution:
    def trap(self, heights: List[int]) -> int:
        left, right = [], []
        
        left.append(heights[0])
        for h in heights[1:]:
            left.append(max(left[-1], h))
        
        right.append(heights[-1])
        for h in reversed(heights[:-1]):
            right.insert(0, max(right[0], h))
            
        result = 0
        
        for i in range(1, len(heights) - 1):
            result += min(left[i], right[i]) - heights[i]
        
        return result
    
# stack
# Time Complexity O(n) 76 ms
# Space Complexity O(n) 15.7 MB
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         result, left_heights = 0, []
#         for current in range(len(height)):
#             while left_heights and (height[left_heights[-1]] < height[current]):
#                 mid_pos = left_heights.pop()
#                 if not left_heights:
#                     break
#                 width = current - left_heights[-1] - 1
#                 water_height = min(height[current], height[left_heights[-1]]) - height[mid_pos]
#                 result += water_height * width
#             left_heights.append(current)
#         return result
                
                
# two pointer
# Time Complexity O(n) 64 ms
# Space Complexity O(n) 15.9 MB
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         left_max, right_max = 0, 0
#         left, right = 0, len(height) - 1
#         result = 0
        
#         while left < right:
#             if height[left] <= height[right]:
#                 # narrow from the left
#                 left_max = max(left_max, height[left])
#                 result += left_max - height[left]
#                 left += 1
#             else:
#                 # narrow from the right
#                 right_max = max(right_max, height[right])
#                 result += right_max - height[right]
#                 right -=1 
#         return result
                