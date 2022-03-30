# Time Complexity O(log mn) 60 ms
# Space Complexity O(m) 14.5 MB
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findFirstIdx(nums: List[int]) -> int:
            left, right = 0, len(nums) - 1
            
            while left < right:
                mid = (left + right) // 2
                
                if nums[mid] == target: return mid
                
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
                    
            return left
        
        first_col_list = [row[0] for row in matrix]
        idx = findFirstIdx(first_col_list)
        idx = idx - 1 if (idx - 1) >= 0 and matrix[idx][0] > target else idx
        final = findFirstIdx(matrix[idx])
        return matrix[idx][final] == target
    

# # Time Complexity O(log mn) 65 ms
# # Space Complexity O(m) 14.5 MB    
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         left, right = 0, len(matrix) * len(matrix[0]) - 1

#         while left <= right:
#             mid = (left + right) // 2
#             y, x = mid // len(matrix[0]), mid % len(matrix[0])

#             if matrix[y][x] == target: return True

#             if matrix[y][x] < target:
#                 left = y * len(matrix[0]) + x + 1
#             else:
#                 right = y * len(matrix[0]) + x - 1
            
#         return False
        
        