# pick a point and make the width wider
# Time Complexity O(n**2) 175 ms
# Space Complexity O(1) 14.6 MB
# class Solution:
#     def maxDistToClosest(self, seats: List[int]) -> int:
#         max_dist = 0
#         for center in range(len(seats)):
#             if seats[center]:
#                 continue
            
#             cur_dist = 0
#             while center - cur_dist >= 0 or center + cur_dist < len(seats):
#                 if center - cur_dist >= 0 and seats[center - cur_dist] != 0:
#                     break
#                 if center + cur_dist < len(seats) and seats[center + cur_dist] != 0:
#                     break
#                 cur_dist += 1
                
#             max_dist = max(max_dist, cur_dist)
#         return max_dist
            
            
# two pointer
# Time Complexity O(n) 124 ms
# Space Complexity O(1) 14.6 MB
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        first, last = 0, 0
        
        max_dist = 0
        while first <= last < len(seats):
            if first == last:
                last += 1
                continue
            if not seats[last]:
                last += 1
            elif seats[first] and seats[last]:
                max_dist = max(max_dist, (last - first) // 2)
                first = last
            elif not seats[first] and seats[last]:
                max_dist = max(max_dist, last - first)
                first = last
                
        if not seats[last - 1]:
            max_dist = max(max_dist, last - first - 1)
            
        return max_dist
    
    
    # check seats where taken
    # Time Complexity O(n) 146 ms
    # Space Complexity O(n) 15MB
    # class Solution:
    #     def maxDistToClosest(self, seats: List[int]) -> int:
    #     sit_seats = [i for i, v in enumerate(seats) if v]
    #     max_dist = max(sit_seats[0], len(seats) - 1 - sit_seats[-1])
    #     for i in range(len(sit_seats) - 1):
    #         max_dist = max(((sit_seats[i + 1] - sit_seats[i])//2), max_dist)
        
    #     return max_dist