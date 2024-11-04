class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        while i < len(word):
            c = word[i]
            count = 1
            i += 1
            while i < len(word) and word[i] == c:
                if count == 9:
                    break
                count += 1
                i += 1
            comp += f"{count}{c}"
        return comp
