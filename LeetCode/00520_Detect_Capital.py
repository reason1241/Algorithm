# Time Complexity O(n): 32 ms
# Space Complexity O(1): 14 MB
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word:
            return True
        if word.lower() == word:
            return True
        if word.capitalize() == word:
            return True
        return False
        
# 36 ms, 13.8 MB
# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         return word.isupper() or word.islower() or word.istitle()