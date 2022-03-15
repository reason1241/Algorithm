# Time Complexity O(n) 676 ms
# Space Complexity O(n) 17.5 MB
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        o, result = 0, []
        for c in s:
            if c == "(":
                o += 1
            elif c == ")":
                if o <= 0:
                    continue
                o -= 1
            result.append(c)

        if o > 0:
            cur_idx = len(result) - 1
            while o > 0 and cur_idx >= 0:
                if result[cur_idx] == "(":
                    result = result[:cur_idx] + result[cur_idx + 1:]
                    o -= 1
                cur_idx -= 1
            
        return "".join(result)
    
# # Time Complexity O(n) 76 ms
# # Space Complexity O(n) 15.9 MB
# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
#         s, st = list(s), []
        
#         for idx, c in enumerate(s):
#             if c == "(":
#                 st.append(idx)
#             elif c == ")":
#                 if st:
#                     st.pop()
#                 else:
#                     s[idx] = ""
        
#         for idx in st:
#             s[idx] = ""
        
#         return "".join(s)
            
                
                    