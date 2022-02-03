from collections import Counter

# Time Complexity O(n**2) 2444 ms
# Space Complexity O(n**2) 15.1 MB
# class Solution:
#     def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
#         def unify_two_dict(nums1: Dict[int, int], nums2: Dict[int, int]) -> Dict[int, int]:
#             result = {}
#             for k1, v1 in nums1.items():
#                 for k2, v2 in nums2.items():
#                     result[k1+k2] = result.get(k1+k2, 0) + (v1 * v2)
#             return result
         
#         step1 = unify_two_dict(Counter(nums1), Counter(nums2))
#         step2 = unify_two_dict(step1, Counter(nums3))
#         result = unify_two_dict(step2, Counter(nums4))
#         return result.get(0, 0)
    

# from collections import Counter

# Time Complexity O(n**2) 757 ms
# Space Complexity O(n**2) 14.3 MB
# class Solution:
#     def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
#         def unify_two_dict(nums1: Dict[int, int], nums2: Dict[int, int]) -> Dict[int, int]:
#             result = {}
#             for k1, v1 in nums1.items():
#                 for k2, v2 in nums2.items():
#                     result[k1+k2] = result.get(k1+k2, 0) + (v1 * v2)
#             return result
         
#         step1 = unify_two_dict(Counter(nums1), Counter(nums2))
#         step2 = unify_two_dict(Counter(nums3), Counter(nums4))
        
#         result = 0
        
#         for k, v in step1.items():
#             result += step2.get(-k, 0) * v
        
#         return result

# from collections import Counter
# Time Complexity O(n**2) 584 ms
# Space Complexity O(n**2) 14.2 MB
# class Solution:
#     def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
#         two_sum = Counter(num1 + num2 for num1 in nums1 for num2 in nums2)
#         return sum(two_sum.get(-(num3 + num4), 0) for num3 in nums3 for num4 in nums4)