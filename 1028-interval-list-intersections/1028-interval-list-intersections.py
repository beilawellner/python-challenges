class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        p1 = p2 = 0

        while p1 < len(firstList) and p2 < len(secondList):
            latest_start = max(firstList[p1][0], secondList[p2][0])
            earliest_end = min(firstList[p1][1], secondList[p2][1])

            if latest_start <= earliest_end:
                res.append([latest_start, earliest_end])

            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1

        return res
