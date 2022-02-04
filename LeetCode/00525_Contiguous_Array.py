# Time Complexity O(n) 1453 ms
# Space Complexity O(n) 19.4 MB
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        current_state, max_len = 0, 0
        diff_map = {0:-1}
        for i, num in enumerate(nums):
            if num == 0:
                current_state -= 1
            else:
                current_state += 1
            
            if current_state not in diff_map:
                diff_map[current_state] = i
            else:
                max_len = max(max_len, i - diff_map[current_state])
        return max_len
            