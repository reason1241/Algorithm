# Time Complexity O(n) 46 ms
# Space Complexity O(n) 13.7 MB
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        num_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for c in s:
            result += num_map[c]
        if ('IV' in s) or ('IX' in s):
            result -= 2
        if ('XL' in s) or ('XC' in s):
            result -= 20
        if ('CD' in s) or ('CM' in s):
            result -= 200
        return result
        
# Time Complexity O(n) 44 ms
# Space Complexity O(n) 13.8 MB                
class Solution:
    def romanToInt(self, s: str) -> int:
        res, prev = 0, 0
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in s[::-1]:
            if dict[i] >= prev:
                res += dict[i]
            else:
                res -= dict[i]
            prev = dict[i]
        return res