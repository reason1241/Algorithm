# Time Complexity O(o * 1) 357 ms, o is the number of operations
# Space Complexity O(10**6 + 1) 40.5 MB
class MyHashSet:
    def __init__(self):
        self.keys = [False] * (10 ** 6 + 1)
        

    def add(self, key: int) -> None:
        self.keys[key] = True
        

    def remove(self, key: int) -> None:
        self.keys[key] = False

    def contains(self, key: int) -> bool:
        return self.keys[key]


# # Time Complexity O(o * l) 183 ms, o is the number of operations l is the maximum length of the list in keys
# # Space Complexity O(n) 18.8 MB
# class MyHashSet:
#     def __init__(self):
#         self.key_len = 997
#         self.keys = [[] for _ in range(self.key_len)]
        
#     def add(self, key: int) -> None:
#         k = key % self.key_len
#         if key not in self.keys[k]:
#             self.keys[k].append(key)
        

#     def remove(self, key: int) -> None:
#         k = key % self.key_len
#         if key in self.keys[k]:
#             self.keys[k].remove(key)

#     def contains(self, key: int) -> bool:
#         k = key % self.key_len
#         return key in self.keys[k]
