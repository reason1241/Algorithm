from collections import defaultdict
from typing import List
# graph problem
# Time Complexity O(n) 732 ms
# Space Complexity O(n) 19.1 MB
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        town = defaultdict(list)
        trusting = [0] * (n + 1)
        for trustor, trustee in trust:
            town[trustee].append(trustor)
            trusting[trustor] += 1
        for i in range(1, n + 1):
            if (len(town[i]) == (n - 1)) and (trusting[i] == 0):
                return i
        return -1
    
# not mine
# we have only one judge if we have
# the only person has n-1 count is a judge
# Time Complexity O(n) 752 ms
# Space Complexity O(n) 18.9 MB
# class Solution:
#     def findJudge(self, N, trust):
#         trusted = [0] * (N+1)
#         for a, b in trust:
#             trusted[a] -= 1
#             trusted[b] += 1

#         for i in range(1, N+1):
#             if trusted[i] == N-1:
#                 return i
#         return -1