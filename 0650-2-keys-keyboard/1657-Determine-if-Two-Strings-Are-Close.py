class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1, d2 = Counter(word1), Counter(word2)
        if set(d1.keys()) != set(d2.keys()):
            return False
        if sorted(d1.values()) != sorted(d2.values()):
            return False
        return True