# make diff map with trips and 0 to 1000
# Time Complexity O(n) 93ms
# Space Complexity O(1) 14.8 MB

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cap_diff = [0] * 1001
        for num, start, dest in trips:
            cap_diff[start] += num
            cap_diff[dest] -= num
            
        cur_passengers = 0
        for i in range(1001):
            cur_passengers += cap_diff[i]
            if cur_passengers > capacity:
                return False
        
        return True
        