# Time Complexity O(n log n) 693 ms
# Space Complexity O(1) 20.9 MB
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        
        left, right = 0, len(people) - 1
        ans = 0
        
        while left <= right:
            temp = people[right]
            right -= 1
            if temp + people[right] <= limit:
                temp += people[right]
                right -= 1
            elif temp + people[left] <= limit and left <= right:
                temp += people[left]
                left += 1
            
            ans += 1
        
        return ans
    
    
# # Time Complexity O(n log n) 592 ms
# # Space Complexity O(1) 20.9 MB    
# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         people = sorted(people)
        
#         left, right = 0, len(people) - 1
#         ans = 0
        
#         while left <= right:
#             if people[left] + people[right] <= limit:
#                 left += 1
#             right -= 1
#             ans += 1
#         return ans