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

        for i, c in enumerate(abbr):
            if c.isdigit():
                if num == 0 and c == '0':
                    return False
                num = (num * 10) + int(c)
            elif c.isalpha():
                if num > 0:
                    p1 += num
                    num = 0
                if p1 >= len(word) or c != word[p1]:
                    return False
                p1 += 1
        if num > 0:
            p1 += num

        return p1 == len(word)
