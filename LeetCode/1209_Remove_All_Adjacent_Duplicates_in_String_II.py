# naive
# Time Complexity O(n ** 2) Timeout
# Space Complexity O(n)
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        def removeDups(input_s: str) -> str:
            s_list = list(input_s)
            in_a_row = 1
            for i in range(1, len(s_list)):
                if s_list[i - 1] == s_list[i]:
                    in_a_row += 1
                    if in_a_row == k:
                        for j in range(- k + 1, 1):
                            s_list[i + j] = ""
                else:
                    in_a_row = 1
            return "".join(s_list)
        
        
        while (new_s := removeDups(s)) != s:
            s = new_s
            
        return new_s
    
# # Time Complexity O(n) 4129 ms
# # Space Complexity O(n) 19.5 MB
# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         value_index = []
#         stack = []
#         for c in s:
#             stack.append(c)
#             if value_index and value_index[-1][0] ==c:
#                 value_index[-1][1] += 1
#                 if value_index[-1][1] == k:
#                     value_index.pop()
#                     stack = stack[:-k]
#             else:
#                 value_index.append([c, 1])
                    
#         return "".join(stack)

# # Time Complexity O(n) 169 ms
# # Space Complexity O(n) 18.6 MB
# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         value_index = []
#         for c in s:
#             if value_index and value_index[-1][0] ==c:
#                 value_index[-1][1] += 1
#                 if value_index[-1][1] == k:
#                     value_index.pop()
#             else:
#                 value_index.append([c, 1])
#         return "".join(c * i for c, i in value_index)

# # Time Complexity O(n) 98 ms
# # Space Complexity O(n) 18.8 MB
# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         value_index = []
#         for c in s:
#             if value_index and value_index[-1][0] ==c:
#                 value_index[-1][1] += 1
#                 if value_index[-1][1] == k:
#                     value_index.pop()
#             else:
#                 value_index.append([c, 1])
#         result = ""
#         for c, i in value_index:
#             result += c * i
#         return result