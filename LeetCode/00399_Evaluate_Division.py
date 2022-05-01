from collections import defaultdict

# Time Complexity O(v + e) 42 ms
# Space Complexity O(v) 13.9 MB
# dfs
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(list)
        
        for fraction, value in zip(equations, values):
            d[fraction[0]].append((fraction[1], value))
            d[fraction[1]].append((fraction[0], 1 / value))
    
        result = []
               
        for q_num, q_denom in queries:
            if (q_num not in d) or (q_denom not in d):
                result.append(float(-1))
                continue
            
            stack = [(q_num, 1)]
            visited = set()
            has_answer = False
            
            while stack:
                cur_denom, cur_val = stack.pop()
                
                if cur_denom == q_denom:
                    result.append(cur_val)
                    has_answer = True
                    break
                
                if cur_denom in visited:
                    continue
                    
                visited.add(cur_denom)
                
                for next_denom, next_val in d[cur_denom]:
                    stack.append((next_denom, cur_val * next_val))
                    
            if not has_answer:
                result.append(float(-1))
                
        return result
                