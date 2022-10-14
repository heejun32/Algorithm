import collections


class Solution:
    '''
    Time Complexity is O(N * M  * 26 * M) -> O(NM^2)
    - N is wordList.lenght
    - M is beginWord.lenght
    Space Complexity is O(N)
    '''
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 검색 속도 향상을 위해
        wordList = set(wordList)

        # bfs
        Q = collections.deque([[beginWord, 1]])
        while Q:
            word, path = Q.popleft()
            if word == endWord:
                return path
            
            for i in range(len(word)):
                for c in "abcdefghijklnmopqrstuvwxyz":
                    searching_word = word[:i] + c + word[i + 1:]
                    if searching_word in wordList:
                        wordList.remove(searching_word)
                        Q.append([searching_word, path + 1])
                        
        # Exception
        return 0