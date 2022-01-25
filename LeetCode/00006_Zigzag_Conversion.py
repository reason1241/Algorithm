# Time Complexity O(n) 60 ms
# Space Complexity O(n) 14.6 MB
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        rows = [ [] for _ in range(numRows) ]
        cur_row, asc = 0, True

        for c in s:
            rows[cur_row].append(c)
            if asc:
                cur_row += 1
                asc = False if cur_row == (numRows - 1) else True
            else:
                cur_row -= 1
                asc = True if cur_row == 0 else False
        
        return "".join(["".join(row) for row in rows])
            
# Time Complexity O(n) 65 ms
# Space Complexity O(n) 14.5 MB
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1: return s
        
#         rows = [ [] for _ in range(numRows) ]
#         cur_row, asc = 0, True

#         for c in s:
#             rows[cur_row].append(c)
#             cur_row += 1 if asc else -1
#             asc = not asc if cur_row == (numRows - 1 ) or cur_row == 0 else asc
        
#         return "".join(["".join(row) for row in rows])
            
        