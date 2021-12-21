from collections import defaultdict

# dp
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = defaultdict(set)
        dp[0].add("")
        dp[1].add("()")
        
        for i in range(2, n + 1):
            for j in dp[i - 1]:
                dp[i].add(f"(){j}")
                dp[i].add(f"({j})")
                dp[i].add(f"{j}()")
            
            remainder = i // 2
            
            for j in range(2, remainder + 1):
                for a in dp[i - j]:
                    for b in dp[j]:
                        dp[i].add(f"{a}{b}")
                        dp[i].add(f"{b}{a}")
            
        return dp[n]


# back tracking
# from collections import defaultdict

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#             ans = []
        
#             def gen(p, left, right):
#                 if not right:
#                     ans.append(p)
                
#                 if left:
#                     gen(p + '(', left - 1, right)
                
#                 if right > left:
#                     gen(p + ')', left, right - 1)
                    
#             gen("", n, n)
#             return ans
