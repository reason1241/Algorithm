# Time Complexity O(n) 51 ms
# Space Complexity O(n) 14.3 MB
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        k_v_dict = {}
        v_set = set()
        if len(pattern) != len(s.split(" ")):
            return False
        
        for k, v in zip(pattern,s.split(" ")):
            if k in k_v_dict:
                if k_v_dict[k] != v:
                    return False
            else:
                if v in v_set:
                    return False
                k_v_dict[k] = v
                v_set.add(v)         
        return True
 

# Time Complexity O(n) 33 ms
# Space Complexity O(n) 14.1 MB       
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        cut_s = s.split(" ")
        k_v_dict = {}
        v_set = set()
        if len(pattern) != len(cut_s):
            return False
        
        for k, v in zip(pattern, cut_s):
            if k in k_v_dict:
                if k_v_dict[k] != v:
                    return False
            else:
                if v in v_set:
                    return False
                k_v_dict[k] = v
                v_set.add(v)         
        return True
    
# Time Complexity O(n) 28 ms
# Space Complexity O(n) 14.4 MB   
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        cut_s = s.split(" ")
        if len(pattern) != len(cut_s):
            return False
        if len(set(pattern)) != len(set(cut_s)):
            return False
        k_v_dict = {}
        
        for k, v in zip(pattern, cut_s):
            if k in k_v_dict:
                if k_v_dict[k] != v:
                    return False
            else:
                k_v_dict[k] = v
        return True
        
        