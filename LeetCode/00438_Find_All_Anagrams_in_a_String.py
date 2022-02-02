from collections import Counter

# Time Complexity O(n) 231 ms
# Space Complexity O(n) 15.3 MB
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_map = Counter(p)
        cur_map = p_map.copy()
        i, cur_len = 0, 0
        while i < len(s):
            cur_char = s[i]
            
            if cur_char not in cur_map:
                i += 1
                cur_map = p_map.copy()
                cur_len = 0
                continue
            
            cur_map[cur_char] -= 1
            cur_len += 1

            if cur_map[cur_char] < 0:
                removed = 0
                start_idx = i - cur_len + 1
                for j in range(start_idx, i):
                    add_char = s[j]
                    cur_map[add_char] += 1
                    cur_len -= 1
                    if add_char == cur_char:
                        break
                i += 1
                continue                
            
            if cur_len == len(p):
                result.append(i -len(p) + 1)
                cur_len -= 1
                bef_char = s[i -len(p) + 1]
                cur_map[bef_char] += 1
                
            i += 1

        return result
    

# use hash
# Time Complexity O(n) 122 ms
# Space Complexity O(1) 15.2 MB
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        hash_s, hash_p, result = 0, 0, []
        for i in range(len(p)): 
            hash_s, hash_p = hash_s + hash(s[i]), hash_p + hash(p[i])
        if hash_s == hash_p: result.append(0)
        for i in range(len(p), len(s)):
            hash_s += hash(s[i]) - hash(s[i - len(p)])
            if hash_s == hash_p: result.append(i - len(p) + 1)
        return result
    
# sliding window with counter
from collections import Counter
# Time Complexity O(n) 898 ms
# Space Complexity O(n) 15.2 MB
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_map = Counter(p)
        window = Counter(s[:len(p)])
        if len(p_map - window) == 0:
            result.append(0)        
        for i in range(len(p), len(s)):
            window[s[i - len(p)]] -= 1
            window[s[i]] += 1
            if len(p_map - window) == 0:
                result.append(i - len(p) + 1)
        return result