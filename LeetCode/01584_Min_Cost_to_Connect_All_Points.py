# Time Complexity O(n ** 2) 2384 ms
# Space Complexity O(n) 14.5 MB
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_dist = [float('inf')] * len(points)
        visited = [False] * len(points)
        
        result = 0
        visit_cnt = 1
        visited[0] = True
        cur_point = 0        
        
        while visit_cnt < len(points):
            cur_x, cur_y = points[cur_point][0], points[cur_point][1]
            
            for i, v in enumerate(points):
                if i == cur_point: continue    
                dist = abs(v[0] - cur_x) + abs(v[1] - cur_y)
                min_dist[i] = min(min_dist[i], dist)
        
            min_point = None
            
            for i, d in enumerate(min_dist):
                if not visited[i]:
                    if not min_point:
                        min_point = i
                    else:
                        if d < min_dist[min_point]:
                            min_point = i
            visit_cnt += 1
            visited[min_point] = True
            result += min_dist[min_point]
            cur_point = min_point
        
        return result
        
# # Time Complexity O(n ** 2) 925 ms
# # Space Complexity O(n) 14.4 MB
# # from https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/1982821/Python-Simple-and-Concise-MST-with-Explanation
# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         d, res = {(x, y): float('inf') if i else 0 for i, (x, y) in enumerate(points)}, 0
#         while d:
#             x, y = min(d, key=d.get)  # obtain the current minimum edge
#             res += d.pop((x, y))      # and remove the corresponding point
#             for x1, y1 in d:          # for the rest of the points, update the minimum manhattan distance
#                 d[(x1, y1)] = min(d[(x1, y1)], abs(x-x1)+abs(y-y1))
#         return res
                