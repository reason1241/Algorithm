# Time Complexity O(n) 300 ms
# Space Complexity O(n) 119.8 MB
# recursive
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            if not num:
                num = "0"
            return str(int(num))
        bef = num[0]
        for i, v in enumerate(num[1:], 1):
            if bef > v:
                return self.removeKdigits(num[:i-1] + num[i:], k - 1)
            bef = v
        return self.removeKdigits(num[:-1], k-1)


# from collections import deque
# # Time Complexity O(n) 72 ms
# # Space Complexity O(n) 14.1 MB
# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         q = deque()
#         while k > 0:
#             if (not q) or (num and q[-1] <= num[0]):
#                 q.append(num[0])
#                 num = num[1:]
#                 continue
#             q.pop()
#             k -= 1
            
#         res = "".join(q) + num if q else "" + num
#         return str(int(res)) if res else "0"
                
                
# # Time Complexity O(n) 36 ms
# # Space Complexity O(n) 14.2 MB                
# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         st = []
#         for n in num:
#             while k and st and st[-1] > n:
#                 st.pop()
#                 k -= 1
#             st.append(n)
#         st = st[:-k] if k else st
#         return "".join(st).lstrip("0") or "0"
                
                
