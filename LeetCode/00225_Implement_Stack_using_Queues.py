# push O(1)
# pop O(n)
# 43 ms, 14 MB
class MyStack:
    
    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.top_val = None

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.top_val = x
        
    def pop(self) -> int:
        n = len(self.q1)
        
        result = self.top_val
    
        for _ in range(n - 1):
            self.top_val = self.q1.pop(0)
            self.q2.append(self.top_val)
            
        self.q1 = self.q2
        self.q2 = []
        
        return result

    def top(self) -> int:
        return self.top_val

    def empty(self) -> bool:
        return len(self.q1) == 0

# # push O(n)
# # pop O(1)
# # 59 ms, 14.1 MB
# class MyStack:
    
#     def __init__(self):
#         self.q1 = []
#         self.q2 = []
#         self.top_val = None

#     def push(self, x: int) -> None:
#         self.q2.append(x)
#         while self.q1:
#             self.q2.append(self.q1.pop(0))
#         self.q1 = self.q2
#         self.q2 = []
        
#     def pop(self) -> int:
#         return self.q1.pop(0)

#     def top(self) -> int:
#         return self.q1[0]

#     def empty(self) -> bool:
#         return len(self.q1) == 0

# # push O(1)
# # pop O(n)
# # 34 ms, 14.1 MB
# class MyStack:
    
#     def __init__(self):
#         self.q = []
#         self.t = None

#     def push(self, x: int) -> None:
#         self.q.append(x)
#         self.t = x
        
#     def pop(self) -> int:
#         n = len(self.q)
        
#         result = self.t
        
#         for _ in range(n - 1):
#             self.t = self.q.pop(0)
#             self.q.append(self.t)
        
#         self.q.pop(0)
        
#         return result

#     def top(self) -> int:
#         return self.t

#     def empty(self) -> bool:
#         return len(self.q) == 0
        