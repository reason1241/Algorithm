# Time Complexity O(n) 250 ms
# Space Complexity O(1) 15.6 MB
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        tip_point = None
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]: return False 
            
            if tip_point is None:
                # ascending
                if arr[i-1] > arr[i]:
                    tip_point = i - 1
            else:
                if arr[i-1] < arr[i]:
                    return False
                
        return tip_point and tip_point != (len(arr) - 1) 

# Time Complexity O(n) 228 ms
# Space Complexity O(1) 15.6 MB
# class Solution:
#     def validMountainArray(self, arr: List[int]) -> bool:
#         if len(arr) < 3: return False
#         first, last = 0, len(arr) - 1
#         while first+1 < len(arr)-1 and arr[first] < arr[first+1]:
#             first += 1
#         while last-1 > 0 and arr[last-1] > arr[last]:
#             last -= 1
#         return first == last
                