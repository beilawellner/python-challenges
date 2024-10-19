class Solution:
    def maximumCoins(self, heroes, monsters, coins):
        ans = [0] * len(heroes)
        monster_and_coin = sorted(zip(monsters, coins), key=lambda x: x[0])
        coins_sum = [0] * len(coins)

        coins_sum[0] = monster_and_coin[0][1]
        for i in range(1, len(coins_sum)):
            coins_sum[i] = coins_sum[i-1] + monster_and_coin[i][1]

        for i, hero in enumerate(heroes):
            ans[i] = self.findTotalCoins(monster_and_coin, hero, coins_sum)
        return ans

    def findTotalCoins(self, monster_and_coin, hero_power, coins_sum):
        l, r = 0, len(monster_and_coin) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if monster_and_coin[mid][0] > hero_power:
                r = mid - 1
            else:
                l = mid + 1

        if l == 0 and monster_and_coin[l][0] > hero_power:
            return 0
        return coins_sum[r]