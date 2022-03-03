# Time Complexity O(n) 80 ms
# Space Complexity O(n) 14.1 MB
# bfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q, start_color = [(sr,sc)], image[sr][sc]
        visited = set()
        while q:
            cur_p = q.pop(0)
            if cur_p in visited:
                continue
            visited.add(cur_p)
            cur_r, cur_c = cur_p
            
            if cur_r < 0 or cur_c < 0 or cur_r >= len(image) or cur_c >= len(image[0]):
                continue
                
            if image[cur_r][cur_c] == start_color:
                image[cur_r][cur_c] = newColor
                q.append((cur_r + 1, cur_c))
                q.append((cur_r - 1, cur_c))
                q.append((cur_r, cur_c + 1))
                q.append((cur_r, cur_c - 1))
                
        return image
    
# Time Complexity O(n) 132 ms
# Space Complexity O(n) 14.2 MB
# dfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == newColor: return image
        
        def dfs(r:int, c:int):
            if image[r][c] == start_color:
                image[r][c] = newColor
                if r > 0: dfs(r-1, c)
                if r < len(image) - 1: dfs(r+1, c)                
                if c > 0: dfs(r, c-1)
                if c < len(image[0]) - 1: dfs(r, c+1)
        
        dfs(sr,sc)
        return image
        