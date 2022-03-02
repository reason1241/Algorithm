from collections import defaultdict, Counter

# Time Complexity O(n**2 log n) 278 ms
# Space Complexity O(n) 21.6 MB
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        
        for s in strs:
            str_map[tuple(sorted(Counter(s).items()))].append(s)
        
        return list(str_map.values())
    
    
# from collections import defaultdict
# # Time Complexity O(n**2) 132 ms
# # Space Complexity O(n) 21.6 MB
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         str_map = defaultdict(list)
        
#         for s in strs:
#             str_map[sum(hash(c) for c in s)].append(s)
                
#         return list(str_map.values())

# # Time Complexity O(n**2 log n) 133 ms
# # Space Complexity O(n) 17.2 MB
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         str_map = defaultdict(list)
        
#         for s in strs:
#             str_map[''.join(sorted(s))].append(s)
                
#         return list(str_map.values())


# # Time Complexity O(n**2 log n) 118 ms
# # Space Complexity O(n) 17.2 MB
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         return [sorted(g) for _, g in itertools.groupby(sorted(strs, key=sorted), sorted)]