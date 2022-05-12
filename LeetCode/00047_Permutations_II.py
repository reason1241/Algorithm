# Time Complexity O(n!) 48 ms
# Space Complexity O(n) 14.5 MB
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def recursivePermute(nums: List[int], selected: List[int]):
            if not nums: 
                result.append(selected)
                return
            
            for idx, num in enumerate(nums):
                if num in nums[:idx]:
                    continue
                recursivePermute(nums[:idx] + nums[idx+1:], selected+[num])
                
        recursivePermute(nums, [])
        return result


# from collections import Counter
# # Time Complexity O(n!) 89 ms
# # Space Complexity O(n) 14.3 MB
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         result = []
        
#         def backtracking(cur: List[int], counter: Dict[int, int]):
#             if len(cur) == len(nums):
#                 result.append(list(cur))
#                 return
            
#             for i, v in counter.items():
#                 if v > 0:
#                     cur.append(i)
#                     counter[i] -= 1
#                     backtracking(cur, counter)
#                     cur.pop()
#                     counter[i] += 1
                
        
#         backtracking([], Counter(nums))
#         return result

# # Time Complexity O(n!) 60 ms
# # Space Complexity O(n) 14 MB
# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         result = [[]]
        
#         for num in nums:
#             new_result = []
#             for sub in result:
#                 for i in range(len(sub) + 1):
#                     new_result.append(sub[:i] + [num] + sub[i:])
#                     if i < len(sub) and sub[i] == num: 
#                         break
#             result = new_result
#         return result