from functools import cache

# Time Complexity O(n) 33 ms
# Space Complexity O(n) 14.2 MB
class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def dp(left_pos: int, available_chars: int) -> int:
            if left_pos <= 1:
                return available_chars
            
            return sum(dp(left_pos - 1, i) for i in range(available_chars, 0, -1))
        
        return dp(n, 5)

# # Time Complexity O(n) 50 ms
# # Space Complexity O(1) 13.9 MB    
# class Solution:
#     def countVowelStrings(self, n: int) -> int:
#         a = e = i = o = u = 1
#         for _ in range(n-1):
#             a = a + e + i + o + u
#             e = e + i + o + u
#             i = i + o + u
#             o = o + u
#             u + u
#         return a + e + i + o + u
    
    
# #https://en.wikipedia.org/wiki/Combination#Number_of_combinations_with_repetition
# #https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)
# from math import comb
# # Time Complexity O(1) 43 ms
# # Space Complexity O(1) 13.9 MB
# class Solution:
#     def countVowelStrings(self, n: int) -> int:
#         return comb(n + 5 - 1, 4)