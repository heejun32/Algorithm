import collections


class Trie:
    
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.count = 0
    
    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
            node.count += 1
    
    def search(self, word: str) -> int:
        node = self
        for idx, char in enumerate(word, 1):
            if node.children[char].count == 1:
                break
            node = node.children[char]

        return idx
    
    def __str__(self):
        return str(self.children) + ' ' + str(self.count)

    
def solution(words):
    answer = 0
    obj = Trie()
    for word in words:
        obj.insert(word)
    for word in words:
        answer += obj.search(word)
    # debugging
    # print(obj)
    return answer