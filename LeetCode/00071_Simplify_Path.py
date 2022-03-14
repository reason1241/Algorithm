# Time Complexity O(n) 42 ms
# Space Complexity O(n) 14 MB
class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        for d in path.split("/"):
            if not d or d == ".": 
                continue
            elif d == "..":
                if result:
                    result.pop(-1)
            else:
                result.append(d)
        
        return f"/{'/'.join(result)}"