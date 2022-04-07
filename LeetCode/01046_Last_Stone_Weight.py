import heapq
# Time Complexity O(n log n) 45 ms
# Space Complexity O(n) 13.8 MB
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            
            if x == y: continue
            
            heapq.heappush(stones, y - x)
            
        return 0 if not stones else -stones[0]
    
    
# import heapq
# # Time Complexity O(n log n) 43 ms
# # Space Complexity O(n) 13.9 MB
# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         stones = [-stone for stone in stones]
#         heapq.heapify(stones)
        
#         while len(stones) > 1:
#             y, x = heapq.heappop(stones), heapq.heappop(stones)          
#             heapq.heappush(stones, y - x)
#         return abs(stones[0])