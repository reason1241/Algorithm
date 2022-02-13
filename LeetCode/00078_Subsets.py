# Time Complexity O(2**n) 56 ms
# Space Complexity O(2**n) 14.1 MB
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def pickN(i: int) -> List[List[int]]:
            result = []
            
            def _pickN(sub: List[int], curr: List[int]):
                if len(curr) == i:
                    result.append(curr)
                
                for idx in range(len(sub)):
                    _pickN(sub[idx+1:], [*curr, sub[idx]])
            
            _pickN(nums, [])
            
            return result
            
        result = []
        
        for i in range(len(nums) + 1):
            result.extend(pickN(i))
        return result
        
# Time Complexity O(2**n) 46 ms
# Space Complexity O(2**n) 14.1 MB
# with cascading
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result, n = [[]], len(nums)

#         for num in nums:
#             result += [curr + [num] for curr in result]
            
#         return result


# Time Complexity O(2**n) 56 ms
# Space Complexity O(n) 14.1 MB
# with backtracking
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(first, curr = []):
#             if len(curr) == k:
#                 output.append(curr[:])
#                 return
#             for i in range(first, n):
#                 curr.append(nums[i])
#                 backtrack(i+1, curr)
#                 curr.pop()
            
#         output, n = [], len(nums)
#         for k in range(n+1):
#             backtrack(0)
#         return output

# Time Complexity O(2**n) 56 ms
# Space Complexity O(n) 14.1 MB
# with bitmask(Lexicographic)
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         result = []
        
#         for i in range(2**n, 2**(n+1)):
#             bitmask = bin(i)[3:]
#             result.append([nums[j] for j in range(n) if bitmask[j]=='1'])
#         return result


# from itertools import combinations
# Time Complexity O(2**n) 63 ms
# Space Complexity O(n) 14 MB
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = []
#         for i in range(len(nums) + 1): result.extend(combinations(nums, i))
#         return result