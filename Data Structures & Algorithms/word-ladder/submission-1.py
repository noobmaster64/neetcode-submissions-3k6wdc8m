class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        queue = deque([(beginWord,1)])
        while queue:
            word,steps = queue.popleft()
            if word == endWord:
                return steps 
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + ch + word[i+1:]

                    if new_word in wordset:
                        queue.append((new_word,steps+1))
                        wordset.remove(new_word)
        
        return 0