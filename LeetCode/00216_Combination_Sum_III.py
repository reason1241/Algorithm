# Time Complexity O(9Ck) 32 ms
# Space Complexity O(9Ck) 14 MB
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k > n: return []
        
        result = []
        def recursive_find(cur: List[int], cur_k: int) -> None:
            if cur_k >= k:
                if sum(cur) == n:
                    result.append(cur)
                return
            
            start_val = cur[-1] if cur else 0
            
            for i in range(start_val + 1, 10):
                recursive_find(cur + [i], cur_k + 1)
    
        recursive_find([], 0)
    
        return result
    
# # Time Complexity O(9Ck) 35 ms
# # Space Complexity O(9Ck) 13.9 MB    
# class Solution:
#     def combinationSum3(self, k: int, n: int) -> List[List[int]]:
#         if k > n: return []
        
#         result = []
#         def recursive_find(cur: List[int], cur_k: int, cur_val: int) -> None:
#             if cur_val > n:
#                 return
            
#             if cur_k >= k:
#                 if cur_val == n:
#                     result.append(cur)
#                 return
            
#             start_val = cur[-1] if cur else 0
            
#             for i in range(start_val + 1, 10):
#                 recursive_find(cur + [i], cur_k + 1, cur_val + i)
    
#         recursive_find([], 0, 0)
    
#         return result
                