# This is python!
# Time complexity O(n) 20 ms
# Space complexity O(1) 14.3 MB
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
        
# Time complexity O(n) 36 ms
# Space complexity O(1) 14.4 MB
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         a2, b2 = 0, 0
#         for i in a:
#             a2 *= 2
#             if i == "1":
#                 a2 += 1
#         for i in b:
#             b2 *= 2
#             if i == "1":
#                 b2 += 1
#         a_p_b = a2 + b2
#         if a_p_b == 0: return "0"
#         result = ""
#         while a_p_b > 0:
#             remainder = a_p_b % 2
#             result = str(remainder) + result
#             a_p_b = a_p_b//2
#         return result