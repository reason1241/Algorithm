# brute force
# timeout
# Time Complexity O(n^2)
# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         pair_cnt = 0
        
#         for i in range(len(time)):
#             for j in range(i + 1, len(time)):
#                 if (time[i] + time[j]) % 60 == 0:
#                     pair_cnt += 1
                    
#         return pair_cnt
        

from collections import Counter
# use hash
# Time Complexity O(n) 224 ms
# Space Complexity O(n) 18 MB
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = Counter(time)
        time_set = set(time)
        
        not_same_pair = 0
        same_pair = 0
        
        for cur_time in time_set:
            pos = 0
            
            while pos < 1000:
                pos += 60
                
                need_time = pos - cur_time
                
                if need_time in counter:
                    if need_time != cur_time:
                        not_same_pair += (counter[need_time] * counter[cur_time])
                    else:
                        if counter[need_time] > 1:
                            same_pair += (counter[need_time] * (counter[need_time] - 1)) / 2
                            
        return int(not_same_pair/2 + same_pair)


# preprocess with modulo operation
# Time Complexity O(n) 260ms
# Space Complexity O(1) 18.4 MB
# from collections import defaultdict
# not mine
# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         result, counter = 0, [0] * 60
#         for i in time:
#             counter[i % 60] += 1
#         for i in range(1, 30):
#             result += counter[i] * counter[60 - i]
#         if counter[0] > 1:
#             result += (counter[0] * (counter[0] - 1)) // 2
#         if counter[30] > 1:
#             result += (counter[30] * (counter[30] - 1)) //2
#         return result


# fill defaultdict
# Time Complexity O(n) 226 ms
# Space Complexity O(1) 17.7 MB
# not mine
# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         d = defaultdict(int)
#         res = 0
#         for song in time:
#             if song % 60 == 0:
#                 res += d[0]
#             else:
#                 res += d[60 - song%60]
                
#             d[song%60]+=1
#         return res