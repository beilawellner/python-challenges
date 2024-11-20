class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for n in range(1, amount + 1):
            for coin in coins:
                if n - coin >= 0:
                    dp[n] = min(dp[n], dp[n - coin] + 1)
        
        return dp[-1] if dp[-1] <= amount else -1