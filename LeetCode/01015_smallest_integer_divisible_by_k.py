# python support very large number over 4bytes
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        base = 1
        cur = 0
        
        remainder_set = set()
        
        for _ in range(k):
            cur += base
            remainder = cur % k
            
            if remainder == 0:
                return len(str(cur))
            
            if remainder in remainder_set:
                return -1
            
            remainder_set.add(remainder)

            base *= 10
            
        return -1


# shorten the code
# Time Complexity O(n) 5420 ms	
# Space Complexity O(1) 14.4 MB	
# class Solution:
#     def smallestRepunitDivByK(self, k: int) -> int:
#         cur_val = 1
#         for length in range(1, k + 1):
#             if cur_val % k == 0:
#                 return length
#             cur_val = (cur_val * 10) + 1
            
#         return -1
    
    
# use remainder
# 1 = a_1 * k + r_1
# 11 = a_2 * k + r_2 = 10(a_1 * k + r_1) + 1 = 10 * a_1 * k + 10 * r_1 + 1
# r_2 = 10(a_1 * k + r_1) - a_2 * k + 1 = k * (10 * a_1 - a_2) + 10 * r_1 + 1
# r_2 = (10 * r_1 + 1) % k
# Time Complexity O(n) 78 ms
# Space Complexity O(1) 13.9 MB
# thus remainder depends on the remainder of the before one
# class Solution:
#     def smallestRepunitDivByK(self, k: int) -> int:
#         cur_val = 1
#         for length in range(1, k + 1):
#             remainder = cur_val % k
#             if remainder == 0:
#                 return length
#             cur_val = (remainder * 10) + 1
            
#         return -1


# add the terminating condition
# If the remainders have a cycle, terminate the checking
# Time Complexity O(n) 52 ms
# Space Complexity O(k) 18 MB
# class Solution:
#     def smallestRepunitDivByK(self, k: int) -> int:
#         cur_val = 1
#         remainder_set = set()
#         for length in range(1, k + 1):
#             remainder = cur_val % k
#             if remainder == 0:
#                 return length
#             if remainder in remainder_set:
#                 return -1
#             remainder_set.add(remainder)
#             cur_val = (remainder * 10) + 1
#         return -1