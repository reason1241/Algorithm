from collections import defaultdict
from typing import List

# bfs
# Time Complexity O(n) 623 ms
# Space Complexity O(n) 28.5 MB
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        vimap = defaultdict(list)
        
        for i, v in enumerate(arr):
            vimap[v].append(i)
        
        seen = set()
        cur_depth,  depth_val = [len(arr) - 1], 0
        
        while cur_depth:
            next_depth = []
            
            for cur_idx in cur_depth: 
                if cur_idx == 0:
                    return depth_val
                if cur_idx in seen:
                    continue
                seen.add(cur_idx)
                if cur_idx + 1 < len(arr):
                    next_depth.append(cur_idx + 1)
                if cur_idx - 1 >= 0:
                    next_depth.append(cur_idx - 1)
                if arr[cur_idx] in vimap:
                    jump_indices = vimap.pop(arr[cur_idx])
                    for jump_idx in jump_indices:
                        if jump_idx != cur_idx:
                            next_depth.append(jump_idx)
            depth_val += 1
            cur_depth = next_depth
                
        return depth_val
        