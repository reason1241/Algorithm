from collections import deque

# Time Complexity O(n**2) Time Limit Exceeded
# Space Complexity O(n)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def canVisit(beginWord: str, nextWord: str) -> bool:
            cnt = 0
            for b, n in zip(beginWord, nextWord):
                if b != n:
                    cnt += 1
            return cnt == 1
        
        if endWord not in wordList: return 0
            
        q, visited = deque([(beginWord, 1)]), set(beginWord)
        
        while q:
            curWord, curLevel = q.popleft()
            
            if curWord == endWord: return curLevel
            
            for word in wordList:  
                if word in visited:
                    continue
                
                if canVisit(curWord, word):
                    visited.add(word)
                    q.append((word, curLevel + 1))
                    
        return 0
            
            
from collections import deque, defaultdict
# Time Complexity O(n) 173 ms
# Space Complexity O(n) 17.5 MB
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:       
        if endWord not in wordList: return 0
        
        searchMap = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                searchMap[word[:i] + "_" + word[i+1:]].append(word)
        
        q, visited = deque([(beginWord, 1)]), set(beginWord)

        while q:
            curWord, curLevel = q.popleft()
            
            if curWord == endWord: return curLevel
            
            travel = []            
            for i in range(len(curWord)):
                key = curWord[:i] + "_" + curWord[i+1:]
                
                if key in searchMap:
                    travel.extend(searchMap[key])
                    del searchMap[key]
            
            for word in travel:
                if word not in visited:
                    q.append((word, curLevel + 1))
                    visited.add(word)
            
        return 0
            
            
        
        
        
        
        
        
        
        