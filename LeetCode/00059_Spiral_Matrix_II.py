# Time Complexity O(n**2) 28 ms
# Space Complexity O(n/2) 14 MB because of the recursion
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        
        def fillMatrix(start_val: int, y: int, x: int , m: int):
            if m == 0: return 
            if m == 1: 
                matrix[y][x] = start_val
                return
            
            cur_val = start_val
            for i in range(4):
                for j in range(m - 1):
                    if i == 0:
                        matrix[y][x + j] = cur_val
                    elif i == 1:
                        matrix[y + j][x + m - 1] = cur_val
                    elif i == 2:
                        matrix[y + m - 1][x + m - 1 - j] = cur_val
                    else:
                        matrix[y + m - 1 - j][x] = cur_val
                    cur_val += 1
          
            fillMatrix(cur_val, y + 1, x + 1, m - 2)
        
        fillMatrix(1, 0, 0, n)
        return matrix

# # Time Complexity O(n**2) 29 ms
# # Space Complexity O(1) 13.8 MB
# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
#         matrix = [[0] * n for _ in range(n)]
        
#         nlayer = n // 2
#         cur_val = 1
        
#         for layer in range(nlayer + 1):            
#             for i in range(n - (layer * 2)):
#                 matrix[layer][i+layer] = cur_val
#                 cur_val += 1

#             for i in range(n - (layer * 2) - 1):
#                 matrix[layer+i+1][-layer-1] = cur_val
#                 cur_val += 1
                
#             for i in range(n - (layer * 2) - 1):
#                 matrix[-layer-1][-layer-i-2] = cur_val
#                 cur_val += 1
                
#             for i in range(n - (layer * 2) - 2):
#                 matrix[-layer-i-2][layer] = cur_val
#                 cur_val += 1
        
#         return matrix
                