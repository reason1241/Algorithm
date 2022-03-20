from collections import Counter

# Time Complexity O(n) 1183 ms
# Space Complexity O(1) 15.1 MB
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        tc, bc = Counter(tops), Counter(bottoms)
        
        for i in range(1, 7):
            if tc[i] + bc[i] >= len(tops):
                for t, b in zip(tops, bottoms):
                    if t != i and b != i:
                        return -1
                return min(len(tops) - tc[i], len(bottoms) - bc[i])
        
        return -1