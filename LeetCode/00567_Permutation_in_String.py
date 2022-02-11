# Time Complexity O(n**2) 3714 ms
# Space Complexity O(1) 13.9 MB
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        if len(Counter(s1) - Counter(s2)) > 0: return False
        for i in range(len(s2) - len(s1) + 1):
            if not len(Counter(s1) - Counter(s2[i:i+len(s1)])):
                return True
        return False
    
# Time Complexity O(n) 721 ms
# Space Complexity O(1) 14 MB
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        s1c, s2c = Counter(s1), Counter(s2)
        if len(s1c - s2c) > 0: return False
        matched = Counter(s2[:len(s1)])
        if len(s1c - matched) == 0: return True
        for i in range(len(s1), len(s2)):
            matched[s2[i]] += 1
            matched[s2[i - len(s1)]] -= 1
            if len(s1c - matched) == 0: return True
        return False