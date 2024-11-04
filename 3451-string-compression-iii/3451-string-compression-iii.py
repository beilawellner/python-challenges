'''
"abcde"
c= a
count = 1
'''
class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        while word:
            c = word[0]
            count = 1
            while count < len(word) and word[count] == c:
                if count == 9:
                    break
                count += 1
            comp += f"{count}{c}"
            word = word[count:]
        return comp