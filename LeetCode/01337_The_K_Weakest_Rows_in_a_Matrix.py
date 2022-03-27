# Time Complexity O(m log m) 112 ms
# Space Complexity O(n) 14.4 MB
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        powers = sorted([(sum(mat[m]), m) for m in range(len(mat))])
        return [p[1] for p in powers[:k]]
    


# Schwartzian transform, one-liner
# Time Complexity O(m log m) 184 ms
# Space Complexity O(n) 14.3 MB
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]



import heapq
# Time Complexity O(m log m) 184 ms
# Space Complexity O(n) 14.3 MB
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = [(sum(mat[i]), i) for i in range(len(mat))]
        heapq.heapify(heap)
        result = []
        
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
            
        return result
    
    
