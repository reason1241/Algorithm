# Time Complexity O(n**2) 451 ms
# Space Complexity O(n**2) 209.4 MB
class Solution:
    def countSubstrings(self, s: str) -> int:        
        def add_palindrome(left_idx: int, right_idx: int):
            while left_idx >= 0 and right_idx < len(s):
                if s[left_idx] != s[right_idx]:
                    break
                result.append(s[left_idx:right_idx+1])
                left_idx -=1
                right_idx += 1
                    
        
        result = []
        
        for i in range(len(s)):
            add_palindrome(i, i)
            add_palindrome(i, i+1)
                
        return len(result)
        
# # Time Complexity O(n**2) 183 ms
# # Space Complexity O(1) 13.9 MB
# class Solution:
#     def countSubstrings(self, s: str) -> int:        
#         def add_palindrome(left_idx: int, right_idx: int):
#             nonlocal result
            
#             while left_idx >= 0 and right_idx < len(s):
#                 if s[left_idx] != s[right_idx]:
#                     break
#                 result += 1
#                 left_idx -=1
#                 right_idx += 1
                    
        
#         result = 0
        
#         for i in range(len(s)):
#             add_palindrome(i, i)
#             add_palindrome(i, i+1)
                
#         return result
        
        
# # Time Complexity O(n**2) 123 ms
# # Space Complexity O(1) 13.7 MB        
# class Solution:
#     def countSubstrings(self, s: str) -> int:        
#         def add_palindrome(left_idx: int, right_idx: int):
#             result = 0
            
#             while left_idx >= 0 and right_idx < len(s) and s[left_idx] == s[right_idx]:
#                 result += 1
#                 left_idx -=1
#                 right_idx += 1
            
#             return result
        
#         return sum(add_palindrome(i,i) + add_palindrome(i, i+1) for i in range(len(s)))

# # Time Complexity O(n**2) 35 ms
# # Space Complexity O(1) 13.9 MB
# class Solution:
#     def countSubstrings(self, s: str) -> int:        
#         center, n = 0, len(s)
        
#         result = 0
        
#         while center < n:
#             right = center + 1
            
#             while right < n and s[center] == s[right]:
#                 right += 1
            
#             result += (right - center + 1) * (right - center) // 2
            
#             next_center = right
            
#             left = center - 1
            
#             while left >= 0 and right < n and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#                 result += 1
            
#             center = next_center
            
#         return result
            

# TODO: Can solve with Manacher's Algorithm