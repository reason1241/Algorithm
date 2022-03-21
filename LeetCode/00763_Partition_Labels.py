from collections import defaultdict

# Time Complexity O(n log n) 40 ms
# Space Complexity O(n) 13.9 MB
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(list)

        for i, c in enumerate(s):
            d[c].append(i)

        total = sorted([(min(l), max(l)) for k, l in d.items()])
        
        result = []
        cur_min, cur_max = 0, 0
        for l, u in total:
            if cur_max < l:
                result.append(s[cur_min:cur_max+1])
                cur_min = l
                cur_max = u
                continue
                
            cur_max = max(cur_max, u)
        result.append(s[cur_min:cur_max+1])
        
        return [len(s) for s in result]
    
    
# Time Complexity O(n) 52 ms
# Space Complexity O(1) 13.8 MB
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {c: i for i, c in enumerate(s)}
        
        result = []
        first = last = 0
        
        for i, c in enumerate(s):
            last = max(last, d[c])
            if i == last:
                result.append(last - first + 1)
                first = i + 1
                
        return result
            
            
            