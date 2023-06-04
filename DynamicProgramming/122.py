from typing import List

# 貪欲法に基づく解法
# 利益が出るところを全部買って、全部売るのが最大の利益になる
# 例えば、[3, 6, 4]と[3, 4, 6]のどちらも同じ利益になる
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_sum = 0
        stock = 10 ** 6
        for i in range(len(prices)):
            # 小さい株を保有
            if prices[i] < stock:
                stock = prices[i]
            
            # 保有額よりも大きければ売る
            profit = prices[i] - stock
            if profit > 0:
                profit_sum += profit
                if i < len(prices) - 1:
                    # 売ったら保有しておく
                    # 次大きくなったらすぐ売る
                    stock = prices[i]
        return profit_sum

# 動的計画法に基づく解法