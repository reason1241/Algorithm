# Time Complexity O(n) 1864 ms
# Space Complexity O(1) 25.1 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p, max_profit = prices[0], 0
        for price in prices:
            min_p = min(price, min_p)
            max_profit = max(price - min_p, max_profit)   
        return max_profit
        
# 1735 ms, 25.1 MB
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         left, right = 0, 1
#         max_price = 0
#         while right < len(prices):
#             if prices[left] > prices[right]:
#                 left = right
#             else:
#                 max_price = max(max_price, prices[right] - prices[left])
#             right += 1
#         return max_price
        

# Time Complexity O(n) 1406 ms
# Space Complexity O(1) 25.1 MB
# class Solution:
#     # kadane's algorithm
#     def maxProfit(self, p):
#         n = len(p)
#         max_so_far, cur = 0, 0
        
#         for i in range(1,n):
#             cur = max(cur + p[i] - p[i-1], 0)
#             max_so_far = max(cur, max_so_far)
#         return max_so_far   
    
    
# Time Complexity O(n) 960 ms
# Space Complexity O(n) 24.6 MB  
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profits = []
#         min_price = prices[0]
#         for price in prices:
#             profits.append(price - min_price)
#             if min_price > price:
#                 min_price = price
#         return max(profits)