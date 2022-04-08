# Time Complexity O(n) 68 ms
# Space Complexity O(n) 14.4 MB
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = [*rooms[0]]
        visited = set([*rooms[0], 0])
        
        while q:
            target = q.pop(0)
                
            for k in rooms[target]:
                if k not in visited:
                    q.append(k)
                    visited.add(k)
        
        return len(visited) == len(rooms)
                