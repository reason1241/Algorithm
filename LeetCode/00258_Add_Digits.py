# Time Complexity O(n) 45 ms
# Space Complexity O(1) 13.9 MB
class Solution:
    def addDigits(self, num: int) -> int:
        return num if num < 10 else self.addDigits(sum(int(i) for i in str(num)))
        
# Time Complexity O(1) 47 ms
# Space Complexity O(1) 13.8 MB
# mathematical way
# the multiple of 9 is always 9 with the digital root
# because sum of multiple of 9 the digits always becomes multiple of 9 (ex. 9, 18, ..., 108, ..., 999)
# so modulo 9 of them is 9 (ex. 999 -> 27 -> 9)
# in other cases like the result of the digital root is 1~8
# for example num = 1000 = 999 + 1 = 9 * 111 + 1
# so 1000 -> 1 = 1000 % 9 = (999) % 9 + 1 % 9
# if num = 527 = 5 * 100 + 2 * 10 + 7
# so 527 -> (5 + 2 + 7 = 14) -> 5
# 527 = 5 * (99 + 1) + 2 * (9 + 1) + 7 = (5 + 2 + 7) + 9 * k
# so 527 % 9 = (5 + 2 + 7) % 9 = 14 % 9 = 5
# if num = 38 = 30 + 8 = 3 * 10 + 8 * 1 = 3 * (9 + 1) + 8 = 3 * 9 + (3 + 8)
# 38 -> 11 -> 2 = 38 % 9
# with the example, you can see that the result of modulo 9 is the digital root value
# class Solution:
#     def addDigits(self, num: int) -> int:
#         if num == 0:
#             return 0
#         if num % 9 == 0:
#             return 9
#         return num % 9        
        

# one-liner for 2
# Time Complexity O(1) 32 ms
# Space Complexity O(1) 13.8 MB
# class Solution:
#     def addDigits(self, num: int) -> int:
#         return 1 + (num - 1) % 9 if num else 0
        