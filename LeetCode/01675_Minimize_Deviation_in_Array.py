import heapq
# Time Complexity O(n log n) 1165 ms
# Space Complexity O(n) 29.9 MB
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        for num in nums:
            tmp = num
            while tmp % 2 == 0: tmp //= 2
            heapq.heappush(pq, (tmp, num))

        result = float('inf')
        max_val = max(odd for odd, _ in pq)
        
        while len(pq) == len(nums):
            val, origin = heapq.heappop(pq)
            result = min(result, max_val - val)
            
            if val % 2 == 1 or val < origin:
                max_val = max(val * 2, max_val)
                heapq.heappush(pq, (val * 2, origin))
                
        return result



# import heapq
# # Time Complexity O(n log n) 1712 ms
# # Space Complexity O(n) 26.3 MB
# # multiply first because odd operation(multiplying) could be executed once
# class Solution:
#     def minimumDeviation(self, nums: List[int]) -> int:
#         pq = []
#         for num in nums:
#             if num & 1: num *= 2
#             heapq.heappush(pq, -num)

#         result = float('inf')
#         min_val = -max(pq)
        
#         while len(pq) == len(nums):
#             val = -heapq.heappop(pq)
#             result = min(result, val - min_val)
            
#             if val % 2 == 0:
#                 min_val = min(val // 2, min_val)
#                 heapq.heappush(pq, -(val // 2))
                
#         return result
            
                

                
# import heapq
# # Time Complexity O(n log n) 1712 ms
# # Space Complexity O(n) 26.3 MB
# # apply heapreplace to optimize the performance(https://docs.python.org/3/library/heapq.html)
# This one step operation is more efficient than a heappop() followed by heappush() and 
# can be more appropriate when using a fixed-size heap. 
# The pop/push combination always returns an element from the heap and replaces it with item.
# class Solution:
#     def minimumDeviation(self, nums: List[int]) -> int:
#         for i in range(len(nums)):
#             if nums[i] % 2 == 1:
#                 nums[i] *= -2
#             else:
#                 nums[i] *= -1
#         heapq.heapify(nums)

#         min_val = -max(nums)
#         result = -nums[0] - min_val
        
#         while -nums[0] % 2 == 0:
#             if -nums[0] // 2 < min_val:
#                 min_val = -nums[0] // 2
#             heapq.heapreplace(nums, nums[0]//2)
#             result = min(-nums[0] - min_val, result)
#         return result
            
                
