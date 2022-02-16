# Time Complexity O(1) 77 ms
# Space Complexity O(1) 13.8 MB
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))
 
# Time Complexity O(n**2) 128 ms
# Space Complexity O(1) 13.9 MB       
# if 123 * 456 = 6 * 3 + 6 * 20 + 6 * 100 + 10 * (5 * 3 + 5 * 20 + 5 * 100) + 100 * (4 * 3 + 4 * 20 + 4 * 100) 
# class Solution:
#     def multiply(self, num1: str, num2: str) -> str:
#         result, pos = 0, 1
#         for n1 in num1[::-1]:
#             pos2 = 1
#             for n2 in num2[::-1]:
#                 result += int(n1) * int(n2) * pos2 * pos
#                 pos2 *= 10
#             pos *= 10
#         return str(result)