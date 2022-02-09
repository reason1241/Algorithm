from collections import Counter

# Time Complexity O(n) 104 ms
# Space Complexity O(n) 17.1 MB
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        if k == 0:
            return len([i for i, v in c.items() if v>= 2])
        
        ns = set(nums)
        result = set()
        
        for n in ns:
            a, b = n + k, n - k
            if a in c:
                result.add((min(a,n), max(a,n)))
            if b in c:
                result.add((min(b,n), max(b,n)))
        return len(result)
                

# from collections import Counter
# # Time Complexity O(n) 98 ms
# # Space Complexity O(n) 17.2 MB
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         c = Counter(nums)
#         if k == 0:
#             return len([i for i, v in c.items() if v>= 2])
        
#         ns = set(nums)
#         result = set()
        
#         for n in ns:
#             a = n + k
#             if a in c:
#                 result.add((a, n) if a < n else (n, a))
            
#         return len(result)


# from collections import Counter
# # Time Complexity O(n) 83 ms
# # Space Complexity O(n) 16.3 MB
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         c = Counter(nums)
#         if k == 0:
#             return len([i for i, v in c.items() if v>= 2])
        
#         ns = set(nums)
#         result = 0
        
#         for n in ns:
#             if n + k in c:
#                 result += 1
            
#         return result
                

# from collections import Counter
# # Time Complexity O(n) 104 ms
# # Space Complexity O(n) 15.7 MB
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         c = Counter(nums)
#         if k == 0:
#             return len([i for i, v in c.items() if v>= 2])
        
#         return sum(1 for i, v in c.items() if k + i in c)