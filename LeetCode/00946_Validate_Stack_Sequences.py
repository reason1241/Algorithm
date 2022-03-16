# Time Complexity O(n) 87 ms
# Space Complexity O(n) 14.1 MB
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        
        while pushed and popped:
            if st and st[-1] == popped[0]:
                st.pop(-1)
                popped.pop(0)
                continue
                        
            st.append(pushed.pop(0))
        
        while st and popped and st[-1] == popped[0]:
            st.pop(-1)
            popped.pop(0)
        
        return not st
            

# # Time Complexity O(n) 76 ms
# # Space Complexity O(n) 14.2 MB            
# class Solution:
#     def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
#         st, i = [], 0
        
#         for v in pushed:
#             st.append(v)
            
#             while st and st[-1] == popped[i]:
#                 st.pop(-1)
#                 i += 1
        
#         return i == len(popped)
            
            
            