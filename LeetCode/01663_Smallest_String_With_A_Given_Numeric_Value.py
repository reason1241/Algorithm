# Time Complexity O(n) 465 ms
# Space Complexity O(1) 15.5 MB
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ""
        
        while k - 26 - (n - 1) > 0:
            k -= 26
            n -= 1
            result += "z"
        
        if n == k:
            return "a" * n + result
        else:
            return "a" * (n-1) + chr(k - (n-1) + 96) + result  
        
# Time Complexity O(n) 59 ms
# Space Complexity O(1) 14.8 MB
# class Solution:
#     def getSmallestString(self, n: int, k: int) -> str:
#         k -= n        
#         z, r = divmod(k, 25)
#         return  'a'*(n-z-1) + chr(ord('a') + r) + 'z'*z if r else 'a'*(n-z) + 'z'*z

        
# # Time Complexity O(n) 40 ms
# # Space Complexity O(1) 15 MB       
# class Solution:
#     def getSmallestString(self, n: int, k: int) -> str:
#         k -= n
#         alpha = '_bcdefghijklmnopqrstuvwxy_'
#         ans = 'z' * (k // 25)
#         if k % 25:
#             ans = alpha[k % 25] + ans
#         return 'a' * (n - len(ans)) + ans
    
# # Time Complexity O(n) 42 ms
# # Space Complexity O(1) 14.8 MB      
# class Solution:
#     def getSmallestString(self, n: int, k: int) -> str:
#         z, alp = divmod(k-n-1, 25)
#         return (n-z-1)*'a'+chr(ord('a')+alp+1)+z*'z'