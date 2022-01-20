import math

# Time Complexity O(nlogn) 480 ms
# Space Complexity O(1) 15.6 MB
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculateEatSum(k: int):
            result = 0
            for pile in piles:
                result += math.ceil(pile / k)
            return result
                
        first, last = 1, max(piles)
        while first < last:
            mid = (first + last) // 2
            if calculateEatSum(mid) <= h:
                last = mid
            else:
                first = mid + 1

        return first
                
        