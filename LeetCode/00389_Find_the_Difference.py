from itertools import zip_longest

# Time Complexity O(n log n) 36 ms
# Space Complexity O(1) 14 MB
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = sorted(s), sorted(t)
        for a, b in zip_longest(s, t):
            if a != b:
                return b


# from collections import Counter

# # Time Complexity O(n) 28 ms
# # Space Complexity O(1) 13.9 MB
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         s, t = Counter(s), Counter(t)
#         for i in t:
#             if s[i] != t[i]:
#                 return i


# from collections import Counter
# # Time Complexity O(n) 36 ms
# # Space Complexity O(1) 13.8 MB
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#     	return list(Counter(t) - Counter(s))[0]

# # Time Complexity O(n) 28 ms
# # Space Complexity O(1) 14 MB
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         c = 0
#         for i in s:
#             c ^= ord(i)
#         for i in t:
#             c ^= ord(i)
#         return chr(c)

# # Time Complexity O(n) 47 ms
# # Space Complexity O(1) 13.8 MB
# class Solution:
#     def findTheDifference(self, s, t):
#         return chr(sum(map(ord, t)) - sum(map(ord, s)))


# # Time Complexity O(n) 77 ms
# # Space Complexity O(1) 13.9 MB
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         for i in set(t):
#             if s.count(i) != t.count(i): return i