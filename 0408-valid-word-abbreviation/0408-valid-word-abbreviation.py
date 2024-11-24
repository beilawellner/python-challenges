'''
"internationalization"
                    -
"i12iz4n"
    -
num = ''
'''
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1 = 0
        num = 0

        i = 0
        while i < len(abbr):
            if abbr[i].isdigit():
                if abbr[i] == '0':
                    return False

                start = i
                while i < len(abbr) and abbr[i].isdigit():
                    i += 1
                num = int(abbr[start:i])
                p1 += num
                num = 0
                # num = (num * 10) + int(c)
            elif abbr[i].isalpha():
                if p1 >= len(word) or abbr[i] != word[p1]:
                    return False
                p1 += 1
                i += 1
        if num > 0:
            p1 += num

        return p1 == len(word)
