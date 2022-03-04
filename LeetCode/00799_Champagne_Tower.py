# Time Complexity O(1) 149 ms
# Space Complexity O(1) 14 MB
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * k for k in range(1, 102)]
        tower[0][0] = poured
        
        for level in range(query_row):
            for idx in range(len(tower[level])):
                if tower[level][idx] > 1:
                    leftover = tower[level][idx] - 1
                    tower[level + 1][idx] += leftover / 2
                    tower[level + 1][idx + 1] += leftover / 2
        
        return 1 if tower[query_row][query_glass] >= 1 else tower[query_row][query_glass]
                
                
        
        
                
                
        
        