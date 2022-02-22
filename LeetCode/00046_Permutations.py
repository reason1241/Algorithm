# Time Complexity O(n!) 44 ms
# Space Complexity O(n!) 14.1 MB
# backtracking
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def _permute(current: List[int], remainders: List[int]):
            if not remainders:
                result.append(current)
                return
            for idx, remainder in enumerate(remainders):
                _permute(current + [remainder], remainders[:idx] + remainders[idx+1:])
        _permute([], nums)
        return result
        


# from itertools import permutations
# # Time Complexity O(n!) 40 ms
# # Space Complexity O(n!) 14.1 MB
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         return permutations(nums)
    
    