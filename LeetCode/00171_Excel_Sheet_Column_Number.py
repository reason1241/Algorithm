# Time Complexity O(n) 45 ms
# Space Complexity I(1) 13.9 MB
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for column in columnTitle:
            result *= 26
            result += ord(column) - 64
        return result
        