# Time Complexity O(n) 196 ms
# Space Complexity O(1) 14.5 MB
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1]:
                n -= 1
                flowerbed[i] = 1
        return n <= 0

