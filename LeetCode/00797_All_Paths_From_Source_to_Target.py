# Time Complexity O(n!) 92 ms
# Space Complexity O(n!) 15.8 MB
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result, dest = [], len(graph) - 1
        
        q = [[0]]
        while q:
            c = q.pop(0)
            
            if c[-1] == dest: 
                result.append(c)
                continue
            
            for n in graph[c[-1]]:
                q.append(c + [n])
        
        return result
        