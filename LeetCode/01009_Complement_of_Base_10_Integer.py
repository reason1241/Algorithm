# use modulo
# Time Complexity O(n) 32 ms
# Space Complexity O(1) 14.3 MB
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        base = 1
        result = 0
        while n > 0:
            cur = 1 - (n % 2)
            result += cur * base
            base <<= 1
            n >>= 1
        return result
    
# import math
# use bitwise operation
# Time Complexity O(n) 32 ms ms
# Space Complexity O(1) 14.1 MB
# class Solution:
#     def bitwiseComplement(self, n: int) -> int:
#         mask = (1 << (int)(math.log(max(n, 1), 2) + 1)) - 1
#         return mask - n

# use bitwise operator to add 1, 35 ms, 14.3 MB
# class Solution:
#     def bitwiseComplement(self, n: int) -> int:
#         if n == 0: return 1
#         mask = 0
#         cur_n = n
#         while cur_n > 0:
#             mask = (mask << 1) | 1
#             cur_n >>= 1
#         return mask ^ n

# use string, 42 ms, 14.3 MB
# class Solution:
#     def bitwiseComplement(self, n: int) -> int:
#         com = bin(n)[2:]
#         result = []
#         for c in com:
#             result.append("1" if c == "0" else "0")
#         return int("".join(result), 2)
        