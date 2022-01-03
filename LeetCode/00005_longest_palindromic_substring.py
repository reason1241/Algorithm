from typing import Tuple

"""
Search from center 2n - 1
Traverse to the outside step by step
e.x.)
The string "a b c" has 5 centers
(a)bc, a()bc, a(b)c, ab()c, ab(c)

From the center, check that if most outside chars are the same.
If so, the string must be a palindrome.
Make the width wider if the string is a palindrome.

time complexity : O(n^2)
space complexity : O(1)(don't need extra spaces)
"""
# search from center
# pick a char or two chars
# For example:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def searchFromCenter(i:int, j: int) -> str:
            while (i > -1) and (j < len(s)):
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
            return s[i+1:j]
    
        max_str = s[0]
        
        for i in range(len(s)):
            cur_str1 = searchFromCenter(i, i)
            cur_str2 = searchFromCenter(i, i + 1)
            if len(cur_str1) > len(max_str):
                max_str = cur_str1
            if len(cur_str2) > len(max_str):
                max_str = cur_str2    
        return max_str
            