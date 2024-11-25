class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur_lst, total):
            if total == target:
                res.append(cur_lst.copy())
                return

            if i >= len(candidates) or total > target:
                return

            cur_lst.append(candidates[i])
            dfs(i, cur_lst, total + candidates[i])
            cur_lst.pop()
            dfs(i + 1, cur_lst, total)

        dfs(0, [], 0)
        return res
