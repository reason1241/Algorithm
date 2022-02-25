import itertools
# Time Complexity O(n) 42 ms
# Space Complexity O(1) 13.9 MB
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vl1, vl2 = version1.split("."), version2.split(".")
        for v1, v2 in itertools.zip_longest(vl1, vl2, fillvalue="0"):
            t1, t2 = v1.lstrip("0"), v2.lstrip("0")
            if t1 == t2:
                continue
            t1 = t1 if t1 else "0"
            t2 = t2 if t2 else "0"
            
            if int(t1) < int(t2):
                return -1
            return 1
        return 
    
# import itertools
# # Time Complexity O(n) 51 ms
# # Space Complexity O(1) 13.9 MB
# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         splits = (map(int, v.split(".")) for v in (version1, version2))
#         for v1, v2 in itertools.zip_longest(*splits, fillvalue=0):
#             if v1 > v2: return 1
#             elif v1 < v2: return -1
#         return 0