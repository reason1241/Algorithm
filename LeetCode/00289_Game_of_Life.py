from itertools import product

# Time Complexity O(mn) 55 ms
# Space Complexity O(mn) 14.4 MB
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_alive(y: int, x: int) -> bool:
            ln = 0
            for dy, dx in product([0,1,-1],[0,1,-1]):
                if dy == dx == 0: continue
                
                if 0 <= dy+y < len(board) and 0 <= dx+x < len(board[0]) and board[dy+y][dx+x]:
                    ln += 1
            if board[y][x]:
                if ln < 2 or ln > 3: 
                    return 0
                else:
                    return 1
            if ln == 3:
                return 1
            return 0
        
        def recursive_update(cur_point):
            if cur_point >= len(board) * len(board[0]): return
            y, x = divmod(cur_point, len(board[0]))
            next_state = is_alive(y, x)
            recursive_update(cur_point + 1)
            board[y][x] = next_state
        
        recursive_update(0)
        
        
# from itertools import product
# # Time Complexity O(mn) 36 ms
# # Space Complexity O(1) 14.1 MB
# class Solution:
#     def gameOfLife(self, board: List[List[int]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
        
#         m, n = len(board), len(board[0])
        
#         for y in range(m):
#             for x in range(n):
#                 ln = 0
#                 for dy, dx in product([0,1,-1],[0,1,-1]):
#                     if dy == dx == 0: continue
#                     ny, nx = dy + y, dx + x
#                     if 0 <= ny < m and 0 <= nx < n and abs(board[ny][nx]) == 1:
#                         ln += 1
#                 if board[y][x] == 1:
#                     if ln < 2 or ln > 3: board[y][x] = -1
#                 else:
#                     if ln == 3: board[y][x] = 2
                        
#         for y in range(m):
#             for x in range(n):
#                 if board[y][x] == -1: board[y][x] = 0
#                 elif board[y][x] == 2: board[y][x] = 1
