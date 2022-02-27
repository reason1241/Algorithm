# Time Complexity O(n) 33 ms
# Space Complexity O(n) 13.9 MB
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(','}':'{',']':'['}
        st = []
        for c in s:
            if c in pairs.keys():
                if not st:
                    return False
                last_char = st.pop()
                if pairs[c] != last_char:
                    return False
            else:
                st.append(c)
        return not st
                