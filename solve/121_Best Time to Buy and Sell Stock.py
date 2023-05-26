"""
O(n^2)로 풀 경우 타임아웃이 걸린다.
최대, 최소를 비교 하면서 선형 시간 내에 풀어야 한다.
"""


import sys

class Solution:
    def maxProfit(self, prices):
        profit = 0
        min_price = sys.maxsize

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            profit = max(profit, prices[i] - min_price)

        return profit

class Solution:
    def maxProfit(self, prices):
        profit = 0
        min_price = 10000

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            profit = max(profit, prices[i] - min_price)

        return profit


if __name__ == "__main__":
    solution = Solution()
    prices = [7,1,5,3,6,4]
    result = solution.maxProfit(prices)

    print(result)