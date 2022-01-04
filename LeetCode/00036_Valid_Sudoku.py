# check vertical, horizontal and 3*3 ways
# Time Complexity: O(1) 92 ms
# Space Complexity: O(1) 14.4 MB
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def hasDuplicate(nums: List[int]) -> bool:
            a_row = [0] * 10
            for num in nums:
                if num.isdigit():
                    num = int(num)
                    a_row[num] += 1
                    if a_row[num] > 1:
                        return True
            return False
        
        for a_row in board:
            if hasDuplicate(a_row):
                return False
        
        for i in range(9):
            a_col = [c[i] for c in board]
            if hasDuplicate(a_col):
                return False
        mid_points = [(1,1), (1,4), (1,7), (4,1), (4,4), (4,7), (7,1), (7,4), (7,7)]
        diffs = [(i,j) for i in range(-1, 2) for j in range(-1,2)]
        for r, c in mid_points:
            a_tile = []
            for d_r, d_c in diffs:
                a_tile.append(board[r + d_r][c + d_c])
            if hasDuplicate(a_tile):
                return False
            
        return True
    
# use zip
# Time, space complexities are same, 108 ms, 14.4 MB
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         def hasDuplicate(nums: List[int]) -> bool:
#             temp = [num for num in nums if num != "."]
#             return len(set(temp)) != len(temp)
        
#         # horizontal
#         for a_row in board:
#             if hasDuplicate(a_row):
#                 return False
        
#         for a_col in zip(*board):
#             if hasDuplicate(a_col):
#                 return False
            
#         for r in (0, 3, 6):
#             for c in (0, 3, 6):
#                 a_tile = [board[i][j] for i in range(r, r+3) for j in range(c, c+3)]    
#                 if hasDuplicate(a_tile):
#                     return False
            
#         return True

# use set
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         total_set = set()
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j].isdigit():
#                     num = board[i][j]
#                     if (('r', i, num) in total_set) or (('c', j, num) in total_set) or ((i//3, j//3, num) in total_set):
#                         return False
#                     total_set.add(('r', i, num))
#                     total_set.add(('c', j, num))
#                     total_set.add((i//3, j//3, num))
#         return True