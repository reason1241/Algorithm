# Time Complexity O(log target) 48 ms
# Space Complexity O(1) 13.9 MB	
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        operations = 0
        while target != startValue:
            if target > startValue:
                if target & 1:
                    target +=1
                else:
                    target >>= 1
            else:
                operations += (startValue - target - 1)
                target += startValue - target
            operations += 1
        return operations
    
    
# # Time Complexity O(log target) 44 ms
# # Space Complexity O(1) 13.9 MB	    
# class Solution:
#     def brokenCalc(self, startValue: int, target: int) -> int:
#         operations = 0
#         while target > startValue:
#             if target & 1:
#                 target +=1
#             else:
#                 target >>= 1
#             operations += 1
                
#         return operations + startValue - target