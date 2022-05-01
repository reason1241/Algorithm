# Time Complexity O(s + t) 33 ms
# Space Complexity O(s + t) 13.8 MB
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def typing(s: str) -> str:
            result = []
        
            for c in s:
                if c == "#":
                    if result:
                        result.pop()
                else:
                    result.append(c)
            
            return "".join(result)
            
        return typing(s) == typing(t)

# # Time Complexity O(s + t) 37 ms
# # Space Complexity O(1) 13.7 MB
# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         def getChar(s: str) -> str:
#             skip = 0
#             for c in reversed(s):
#                 if c == "#":
#                     skip += 1
#                 elif skip:
#                     skip -= 1
#                 else:
#                     yield c
#         return all(x == y for x, y in itertools.zip_longest(getChar(s), getChar(t)))
                