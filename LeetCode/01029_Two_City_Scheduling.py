# Time Complexity O(n log n) 59 ms
# Space Complexity O(n) 13.9 MB
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = [(max(v[0],v[1]) - min(v[0],v[1]), i) for i, v in enumerate(costs)]
        diffs.sort(reverse=True)
               
        ans, a, b = 0, 0, 0

        for _, idx in diffs:
            if costs[idx][0] < costs[idx][1]:
                if a < len(costs) // 2:
                    a += 1
                    ans += costs[idx][0]
                else:
                    b += 1
                    ans += costs[idx][1]
            elif costs[idx][0] > costs[idx][1]:
                if b < len(costs) // 2:
                    b += 1
                    ans += costs[idx][1]
                else:
                    a += 1
                    ans += costs[idx][0]
        
            else:
                if a < len(costs) // 2:
                    a += 1
                    ans += costs[idx][0]
                else:
                    b += 1
                    ans += costs[idx][1]                    
        
        return ans
    
# # Time Complexity O(n log n) 48 ms
# # Space Complexity O(n) 13.9 MB    
# class Solution:
#     def twoCitySchedCost(self, costs: List[List[int]]) -> int:
#         costs.sort(key=lambda x: x[0] - x[1])
#         ans = 0
#         for i in range(len(costs) // 2):
#             ans += costs[i][0]
            
#         for i in range(len(costs) // 2, len(costs)):
#             ans += costs[i][1]            
        
#         return ans

# # Time Complexity O(n log n) 63 ms
# # Space Complexity O(n) 13.8 MB    
# class Solution:
#     def twoCitySchedCost(self, costs: List[List[int]]) -> int:
#         ans = sum(i[0] for i in costs)
#         pay_back = sorted([i[0] - i[1] for i in costs], reverse=True)
#         return ans - sum(pay_back[:len(costs) // 2])
        
        
        
        
        