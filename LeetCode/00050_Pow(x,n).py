# Time Complexity 60 ms
# Space Complexity 13.8 MB
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n
    

# Time Complexity O(log n) 28 ms
# Space Complexity O(1) 14 MB
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if not n:
#             return 1
#         if n < 0:
#             return 1 / self.myPow(x, -n)
#         if n % 2 == 0:
#             return self.myPow(x * x, n // 2)
#         return self.myPow(x, n - 1) * x
        