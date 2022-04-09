from collections import Counter
# Time Complexity O(n + d log d) d is unique elements in array 92 ms
# Space Compexity O(n) 18.7 MB
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return [v[0] for v in sorted(c.items(), key=lambda x: -x[1])[:k]]
    
    
    
# import heapq
# # Time Complexity O(n + d log d) d is unique elements in array 139 ms
# # Space Compexity O(n) 18.8 MB
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         c = Counter(nums)
#         freq = [(v, k) for k, v in c.items()]
#         heapq.heapify(freq)
#         return [k for v, k in heapq.nlargest(k, freq)]
    
    
    
# import heapq
# # Time Complexity O(n + d log d) d is unique elements in array 119 ms
# # Space Compexity O(n) 18.6 MB
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         if k == len(nums): return nums
#         c = Counter(nums)
#         return heapq.nlargest(k, c.keys(), key=c.get)
    
    
# # Can be solved with Quickselect
# # https://en.wikipedia.org/wiki/Quickselect
# Copy from the solution
# Time Complexity O(n) 120 ms
# Space Complexity O(n) 18.8 MB
# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = Counter(nums)
#         unique = list(count.keys())
        
#         def partition(left, right, pivot_index) -> int:
#             pivot_frequency = count[unique[pivot_index]]
#             # 1. move pivot to end
#             unique[pivot_index], unique[right] = unique[right], unique[pivot_index]  
            
#             # 2. move all less frequent elements to the left
#             store_index = left
#             for i in range(left, right):
#                 if count[unique[i]] < pivot_frequency:
#                     unique[store_index], unique[i] = unique[i], unique[store_index]
#                     store_index += 1

#             # 3. move pivot to its final place
#             unique[right], unique[store_index] = unique[store_index], unique[right]  
            
#             return store_index
        
#         def quickselect(left, right, k_smallest) -> None:
#             """
#             Sort a list within left..right till kth less frequent element
#             takes its place. 
#             """
#             # base case: the list contains only one element
#             if left == right: 
#                 return
            
#             # select a random pivot_index
#             pivot_index = random.randint(left, right)     
                            
#             # find the pivot position in a sorted list   
#             pivot_index = partition(left, right, pivot_index)
            
#             # if the pivot is in its final sorted position
#             if k_smallest == pivot_index:
#                  return 
#             # go left
#             elif k_smallest < pivot_index:
#                 quickselect(left, pivot_index - 1, k_smallest)
#             # go right
#             else:
#                 quickselect(pivot_index + 1, right, k_smallest)
         
#         n = len(unique) 
#         # kth top frequent element is (n - k)th less frequent.
#         # Do a partial sort: from less frequent to the most frequent, till
#         # (n - k)th less frequent element takes its place (n - k) in a sorted array. 
#         # All element on the left are less frequent.
#         # All the elements on the right are more frequent.  
#         quickselect(0, n - 1, n - k)
#         # Return top k frequent elements
#         return unique[n - k:]