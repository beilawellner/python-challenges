class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        spaces = [index for index, char in enumerate(sentence) if char == ' ']
        if spaces:
            for space in spaces:
                if sentence[space-1] != sentence[space+1]:
                    return False
        return sentence[-1] == sentence[0]
