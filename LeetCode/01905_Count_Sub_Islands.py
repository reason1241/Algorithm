# Time Complexity O(n) 3574 ms because we traverse matrix points once(actually not once but we change the point 1 -> 0 when we traveled and we escape right after the visitng when we meet 0)
# Space Complexity O(n) 81.4 MB because of stack calls
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def sink(y: int, x: int) -> bool:
            if y < 0 or y >= len(grid2) or x < 0 or x >= len(grid2[0]) or grid2[y][x] == 0: return True            
            if grid1[y][x] == 0: return False
            
            grid2[y][x] = 0
            
            return all((sink(y + 1, x), sink(y - 1, x), sink(y, x + 1), sink(y, x - 1)))
            
        ans = 0
        for y, row in enumerate(grid2):
            for x, val in enumerate(row):
                if val and sink(y, x):
                    ans += 1
        return ans
            