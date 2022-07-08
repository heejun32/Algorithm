from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = []
        for word in re.sub(r'[^\w]', ' ', paragraph).lower().split():
            if word not in banned:
                words.append(word)

        words_dict = Counter(words)
        return words_dict.most_common(1)[0][0]
