import uuid

# Time Complexity O(n) 57 ms
# Space Complexity O(n) 14.5 MB
class Codec:
    def __init__(self):
        self.db = {}
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = uuid.uuid4().hex[:5]
        self.db[key] = longUrl
        return key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.db[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


# # Time Complexity O(n) 57 ms
# # Space Complexity O(n) 14.5 MB
# class Codec:
    
#     def encode(self, longUrl: str) -> str:
#         """Encodes a URL to a shortened URL.
#         """
#         return longUrl

#     def decode(self, shortUrl: str) -> str:
#         """Decodes a shortened URL to its original URL.
#         """
#         return shortUrl