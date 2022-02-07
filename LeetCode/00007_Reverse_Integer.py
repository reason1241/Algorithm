# Time Complexity O(n) 34 ms
# Space Complexity O(1) 13.9 MB
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)[::-1]
        if x[-1] == '-':
            return -int(x[:-1]) if -int(x[:-1]) > -(2**31) else 0
        return int(x) if int(x) < 2**31 - 1 else 0
    
# # Time Complexity O(n) 50 ms
# # Space Complexity O(1) 13.9 MB
# class Solution:
#     def reverse(self, x: int) -> int:
#         sign = [1, -1][x < 0]
#         result = int(str(abs(x))[::-1]) * sign
#         return result if -(2**31) <= result <= (2**31 - 1) else 0