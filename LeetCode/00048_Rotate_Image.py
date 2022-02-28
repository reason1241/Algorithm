# Time Complexity O(n) 36 ms
# Space Complexity O(1) 13.9 MB

class Solution:
    """
        3 * 3
        (0,0) -> (0,2)  
        (0,1) -> (1,2)
        (0,2) -> (2,2)
        
        (1,0) -> (1,1)
        (1,1) -> (1,1)
        (1,2) -> (2,1)
        
        (2,0) -> (0,0)
        (2,1) -> (1,0)
        (2,2) -> (2,0)
        ----
        (0,0) -> (0,2) 
        (0,2) -> (2,2)
        (2,2) -> (2,0)
        (2,0) -> (0,0)
        
        (0,1) -> (1,2)
        (1,2) -> (2,1)
        (2,1) -> (1,0)
        (1,0) -> (1,1)
        
        Original point as (y,x), New point is (x, 2-y)
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        def _rotate(x: int, y: int, max_idx: int):
            point_vals = {}
            cur_y, cur_x = y, x
            
            for i in range(4):
                next_y, next_x = cur_x, max_idx - cur_y
                point_vals[(next_y, next_x)] = matrix[next_y][next_x]
                cur_y, cur_x = next_y, next_x
            
            for i in range(4):
                next_y, next_x = cur_x, max_idx - cur_y
                matrix[next_y][next_x] = point_vals[(cur_y, cur_x)]
                cur_y, cur_x = next_y, next_x
            
        depths, max_idx = ceil(len(matrix[0]) / 2), len(matrix[0]) - 1
        for y in range(depths):
            for x in range(max_idx - (y * 2)):
                _rotate(x+y, y, max_idx)
        return matrix
