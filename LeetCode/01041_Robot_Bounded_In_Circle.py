# If robot returns to it's base point => true
# or if the robot doesn't look the same direction after the process => true
# Time Complexity O(n) 31 ms
# Space Complexity O(1) 14.3 MB
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions, cur_point = [(1,0),(0,-1),(-1,0),(0,1)], 0
        cur_y, cur_x = 0, 0
        for instruction in instructions:
            if instruction == 'L':
                cur_point = (cur_point + 3) % 4
            elif instruction == 'R':
                cur_point = (cur_point + 1) % 4
            else:
                cur_y += directions[cur_point][0]
                cur_x += directions[cur_point][1]
                
        return (cur_y == cur_x == 0) or (cur_point != 0)

# same but changing the logic to check the direction
# 40 ms, 14.1 MB
# class Solution:
#     def isRobotBounded(self, instructions: str) -> bool:
#         direction = (1,0)
#         cur_y, cur_x = 0, 0
#         for instruction in instructions:
#             if instruction == 'L':
#                 direction = (direction[1], -direction[0])
#             elif instruction == 'R':
#                 direction = (-direction[1], direction[0])
#             else:
#                 cur_y, cur_x = cur_y + direction[1], cur_x + direction[0]
                
#         return (cur_y == cur_x == 0) or (direction != (1,0))