"""
You are given an array prices where prices[i] is the price of a given stock on ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day
in the future to sell that stock.
Return the maximum profit you can achieve from this transaction, If you cannot achieve any profit,
return 0.
"""

from typing import List


def maxProfit(prices: List[int]) -> int:
    p1 = 0
    p2 = 1

    max_profit = 0

    while p1 < len(prices) - 1 and p2 <= len(prices) - 1:
        if prices[p1] > prices[p2]:
            p1 = p2
            p2 = p1 + 1
        else:
            if prices[p2] - prices[p1] > max_profit:
                max_profit = prices[p2] - prices[p1]
            
            p2 += 1

    return max_profit

# Test cases
prices = [1,2]
assert maxProfit(prices) == 5  # Buy at 1, sell at 6, profit = 5

prices = [7,6,4,3,1]
assert maxProfit(prices) == 0  # Prices only decrease, no profit possible