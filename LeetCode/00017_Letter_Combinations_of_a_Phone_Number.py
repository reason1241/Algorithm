# Time Complexity O(n**d) 24 ms
# Space Complexity O(n**d) 14.4 MB
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        letter_map = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        
        result = []
        
        def recursiveAdder(sub_digits: str, current_str: str):    
            if len(sub_digits) < 1:
                result.append(current_str)
                return
                           
            for c in letter_map[sub_digits[0]]:
                recursiveAdder(sub_digits[1:], current_str + c)
                
        recursiveAdder(digits, "")
        
        return result
    
# # Time Complexity O(n**d) 35 ms
# # Space Complexity O(n**d) 13.8 MB    
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         d = {
#             '2':['a','b','c'],
#             '3':['d','e','f'],
#             '4':['g','h','i'],
#             '5':['j','k','l'],
#             '6':['m','n','o'],
#             '7':['p','q','r','s'],
#             '8':['t','u','v'],
#             '9':['w','x','y','z']
#         }
#         result = []
        
#         for c in digits:
#             new_result = []
            
#             if not result:
#                 for n in d[c]:
#                     new_result.append(n)
#             else:
#                 for n in d[c]:
#                     for o in result:
#                         new_result.append(o + n)
#             result = new_result
        
#         return result
            
# # Time Complexity O(n**d) 27 ms
# # Space Complexity O(n**d) 13.9 MB             
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         d = {
#             '2':'abc', '3':'def',
#             '4':'ghi', '5':'jkl',
#             '6':'mno', '7':'pqrs',
#             '8':'tuv', '9':'wxyz'
#         }
#         result = [""]
        
#         for c in digits:
#             result = [i + j for i in result for j in d[c]]
        
#         if result[0] == "":
#             result = []
        
#         return result