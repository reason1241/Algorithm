# Time Complexity O(n) 26 ms
# Space Complexity O(1) 14 MB
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:       
        s_point = 0
        for c in t:
            if s_point >= len(s):
                break
            
            if s[s_point] == c:
                s_point += 1
                
        return s_point == len(s)