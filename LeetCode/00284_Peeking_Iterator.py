# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

# Time Complexity O(n) 32 ms
# Space Complexity O(1) 14 MB
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.peek_val = None
        self.iterator = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peek_val:
            return self.peek_val
        
        self.peek_val = self.iterator.next()
        return self.peek_val
        
        

    def next(self):
        """
        :rtype: int
        """
        if self.peek_val:
            result = self.peek_val
            self.peek_val = None
            return result
        return self.iterator.next()
            
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peek_val:
            return True
        return self.iterator.hasNext()
    
# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].