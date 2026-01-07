from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        
        if total_len > len(s):
            return []
        
        word_count = Counter(words)
        result = []
        
        for i in range(len(s) - total_len + 1):
            window = s[i:i + total_len]
            chunks = [window[j:j + word_len] for j in range(0, total_len, word_len)]
            if Counter(chunks) == word_count:
                result.append(i)
        
        return result