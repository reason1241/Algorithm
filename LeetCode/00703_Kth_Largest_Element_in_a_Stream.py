# Time Complexity O(n * log n + a * n log n) 1107 ms
# Space Complexity O(n) 18.2 MB
class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]
    

# # Time Complexity O(n * log n + a * n log n 752 ms
# # Space Complexity O(n) 18.2 MB    
# class KthLargest:
    
#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.nums = sorted(nums)[-k:]

#     def add(self, val: int) -> int:
#         if not self.nums or len(self.nums) < self.k or val > self.nums[0]:
#             self.nums.append(val)
#             self.nums.sort()
#             self.nums = self.nums[-self.k:]
#         return self.nums[0]
    
    

# import heapq
# # Time Complexity O(n * log n + a * log n) 133 ms
# # Space Complexity O(n) 18.1 MB
# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         heapq.heapify(nums)
#         self.nums = nums
        
#         while len(self.nums) > k:
#             heapq.heappop(self.nums)
        

#     def add(self, val: int) -> int:        
#         if len(self.nums) >= self.k and val <= self.nums[0]:
#             return self.nums[0]
        
#         heapq.heappush(self.nums, val)
        
#         while len(self.nums) > self.k:
#             heapq.heappop(self.nums)
            
#         return self.nums[0]
        
    
# import heapq
# # Time Complexity O(n * log n + a * log n) 112 ms
# # Space Complexity O(n) 18.2 MB
# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         heapq.heapify(nums)
#         self.nums = nums
        
#         while len(self.nums) > k:
#             heapq.heappop(self.nums)
        

#     def add(self, val: int) -> int:        
#         if len(self.nums) < self.k:
#             heapq.heappush(self.nums, val)
#         elif self.nums[0] < val:
#             heapq.heappushpop(self.nums, val)
               
#         return self.nums[0]
        
    
    
# from sortedcontainers import SortedList
# # Time Complexity O(n * log n) 195 ms
# # Space Complexity O(n) 18.9 MB
# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.sorted_list = SortedList(nums)
            

#     def add(self, val: int) -> int:        
#         self.sorted_list.add(val)
#         return self.sorted_list[-self.k]
    