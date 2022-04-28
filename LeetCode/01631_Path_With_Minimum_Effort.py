import heapq

# Time Complexity O(rc log rc) 758 ms
# Space Complexity O(rc) 16.5 MB
class Solution:
    # dijkstra
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        h = [(0, 0, 0)]
        visited = set()
        
        while h:
            cost, y, x = heapq.heappop(h)
                        
            if y == rows - 1 and x == cols - 1:
                return cost
            
            if (y, x) in visited:
                continue
            
            visited.add((y, x))
            
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= y + dy < rows and 0 <= x + dx < cols and (dy + y, dx + x) not in visited:
                    next_cost = abs(heights[y][x] - heights[dy + y][dx + x])
                    heapq.heappush(h, (max(cost, next_cost), y + dy, x + dx))
                
        return -1
        