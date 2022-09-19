import collections


class TrieNode:
    
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.count = 0
        

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
            node.count += 1
            # print(char, node.count)
            
    def search(self, word: str) -> int:
        node = self.root
        count = 0
        for char in word:
            if node.count == 1:
                return count
            count += 1
            node = node.children[char]
            
        return count

def solution(words):
    answer = 0
    trie = Trie()
    
    for word in words:
        trie.insert(word)
    for word in words:
        answer += trie.search(word)
        
    return answer