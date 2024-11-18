'''
code = [5,7,1,4], k = 3
        s
              e
code = [5,7,1,4], k = -3
        s
              e
res  = [0,0,0,0]
'''
class Solution:
    # sliding window
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        if k == 0:
            return res
        if k > 0:
            start, end = 1, k
        else:
            start, end = n + k, n - 1
        win_sum = sum(code[i % n] for i in range(start, end + 1))
        for i in range(n):
            res[i] = win_sum
            win_sum -= code[start % n]
            start += 1
            end += 1
            win_sum += code[end % n]
        return res
            


    # # # # # # # # # # # # Brute Force
    # def decrypt(self, code: List[int], k: int) -> List[int]:
    #     result = [0] * len(code)
    #     if k == 0:
    #         return result
    #     for i in range(len(result)):
    #         if k > 0:
    #             for j in range(i + 1, i + k + 1):
    #                 result[i] += code[j % len(code)]
    #         else:
    #             for j in range(i + k, i):
    #                 result[i] += code[(j + len(code)) % len(code)]
    #     return result
