class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if prices[i] > prices[j]:
                    continue
                profit = prices[j] - prices[i]
                print(profit)
                res = max(res, profit)
        return res