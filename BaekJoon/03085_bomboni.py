import sys

# brute force
# Time Complexity O(n^3) 3428ms
# Space Complexity O(n^2) 31956kb
import sys
from collections import Counter

# brute force
n = int(sys.stdin.readline().strip())
candy_map = [list(sys.stdin.readline().strip()) for _ in range(n)]

max_val = 0

def map_swap(r1, c1, r2, c2):
    temp = candy_map[r1][c1]
    candy_map[r1][c1] = candy_map[r2][c2]
    candy_map[r2][c2] = temp

def count_in_row_max(input_list):
    max_val = 0
    bef, cur_val = None, 0
    for cur in input_list:
        if cur != bef:
            bef = cur
            cur_val = 1
        else: 
            cur_val += 1
        max_val = max(max_val, cur_val)
    return max_val
        


def find_max_candy():
    temp_max = 0
    # check horizontally
    for row_list in candy_map:
        temp_max = max(temp_max, count_in_row_max(row_list))
            
    # check vertically
    for col in range(n):
        col_list = [row_list[col] for row_list in candy_map]
        temp_max = max(temp_max, count_in_row_max(col_list))
            
    return temp_max

# change horizontally
for row in range(n):
    for col in range(n-1):
        if candy_map[row][col] != candy_map[row][col + 1]:
            map_swap(row, col, row, col + 1)
            max_val = max(find_max_candy(), max_val)
            map_swap(row, col, row, col + 1)
        
        
# change vertically
for row in range(n-1):
    for col in range(n):
        if candy_map[row + 1][col] != candy_map[row][col]:
            map_swap(row, col, row + 1, col)
            max_val = max(find_max_candy(), max_val)
            map_swap(row, col, row + 1, col)
        
print(max_val)


# # improve performance
# # check all of the map
# # and in the procedure, if you swap two candies, check only 3 lines that the modification effects
# import sys

# # brute force
# # Time Complexity O(n^3) 168ms
# # Space Complexity O(n^2) 29200kb
# n = int(sys.stdin.readline().strip())
# candy_map = [list(sys.stdin.readline().strip()) for _ in range(n)]

# def map_swap(r1, c1, r2, c2):
#     temp = candy_map[r1][c1]
#     candy_map[r1][c1] = candy_map[r2][c2]
#     candy_map[r2][c2] = temp

# def count_in_row_max(input_list):
#     max_val = 0
#     bef, cur_val = None, 0
#     for cur in input_list:
#         if cur != bef:
#             bef = cur
#             cur_val = 1
#         else: 
#             cur_val += 1
#         max_val = max(max_val, cur_val)
#     return max_val
        


# def find_max_candy():
#     temp_max = 0
#     # check horizontally
#     for row_list in candy_map:
#         temp_max = max(temp_max, count_in_row_max(row_list))
            
#     # check vertically
#     for col in range(n):
#         col_list = [row_list[col] for row_list in candy_map]
#         temp_max = max(temp_max, count_in_row_max(col_list))
            
#     return temp_max

# def find_max_candy_partial(r1, c1, r2, c2):
#     temp_max = 0
    
#     if r1 != r2:
#         temp_max = max(count_in_row_max(candy_map[r1]), count_in_row_max(candy_map[r2]))
#         temp_max = max(temp_max, count_in_row_max([row_list[c1] for row_list in candy_map]))
#     else:
#         temp_max = max(count_in_row_max([row_list[c1] for row_list in candy_map]), count_in_row_max([row_list[c2] for row_list in candy_map]))
#         temp_max = max(temp_max, count_in_row_max(candy_map[r1]))
    
#     return temp_max

# max_val = find_max_candy()

# # change horizontally
# for row in range(n):
#     for col in range(n-1):
#         if candy_map[row][col] != candy_map[row][col + 1]:
#             map_swap(row, col, row, col + 1)
#             max_val = max(max_val, find_max_candy_partial(row, col, row, col + 1))
#             map_swap(row, col, row, col + 1)
        
        
# # change vertically
# for row in range(n-1):
#     for col in range(n):
#         if candy_map[row + 1][col] != candy_map[row][col]:
#             map_swap(row, col, row + 1, col)
#             max_val = max(max_val, find_max_candy_partial(row, col, row + 1, col))
#             map_swap(row, col, row + 1, col)
        
# print(max_val)