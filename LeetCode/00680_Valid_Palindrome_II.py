# Time Complexity O(n) 197 ms
# Space Complexity O(1) 14.6 MB
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while s[left] == s[right] and left < right:
            left += 1
            right -= 1
            
        if left == right or left > right: return True    
        
        n_l, n_r = left + 1, right
        
        while s[n_l] == s[n_r] and n_l < n_r:
            n_l += 1
            n_r -= 1
            
        if n_l == n_r or n_l > n_r: return True 
        
        n_l, n_r = left, right - 1
        
        while s[n_l] == s[n_r] and n_l < n_r:
            n_l += 1
            n_r -= 1
            
        if n_l == n_r or n_l > n_r: return True 
    
        return False
    
# # Time Complexity O(n) 92 ms
# # Space Complexity O(1) 14.5 MB    
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         left, right = 0, len(s) - 1
        
#         while left < right:
#             if s[left] != s[right]:
#                 return (s[left+1:right+1] == s[left+1:right+1][::-1] or
#                         s[left:right] == s[left:right][::-1])

#             left += 1
#             right -= 1
            
#         return True