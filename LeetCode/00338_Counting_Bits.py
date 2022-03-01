# Time Complexity O(n**2) 331 ms
# Space Complexity O(n) 20.8 MB
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            cnt = 0
            while i > 0:
                b = i % 2
                cnt += 1 if b else 0
                i = i // 2
            result.append(cnt)
        return result

# # Time Complexity O(n) 88 ms
# # Space Complexity O(n) 20.7 MB
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         result, cur_bi = [0, 1], 1
#         for i in range(2, n+1):
#             if i == cur_bi * 2:
#                 cur_bi = i
#             result.append(result[i % cur_bi] + 1)
#         return result[:n+1]
    
# # Time Complexity O(n) 80 ms
# # Space Complexity O(n) 20.7 MB
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         result = [0]
#         while len(result) < n+1:
#             result.extend([i+1 for i in result])
#         return result[:n+1]