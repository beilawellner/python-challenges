class Solution:
    def compress(self, chars: List[str]) -> int:
        i, res = 0, 0
        while i < len(chars):
            cur_len = 1
            while i + cur_len < len(chars) and chars[i] ==chars[i+cur_len]:
                cur_len += 1
            chars[res] = chars[i]
            res += 1
            if cur_len > 1:
                str_len = str(cur_len)
                chars[res:res+len(str_len)] = list(str_len)
                res += len(str_len)
            i += cur_len
        return res
        