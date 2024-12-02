class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        count = [0] * (max(nums) + 1 + k)
        for num in nums:
            count[num] += 1

        prefix = [count[0]]

        for cnt in count[1:]:
            prefix.append(prefix[-1] + cnt)

        ans = 0

        for i in range(len(count) - k):
            left = max(0, i - k - 1)
            right = min(len(count) - 1, i + k)
            mid = count[i]

            to_convert = prefix[right] - prefix[left] - mid

            if to_convert >= numOperations:
                ans = max(ans, mid + numOperations)
            else:
                ans = max(ans, mid + to_convert)

        return ans