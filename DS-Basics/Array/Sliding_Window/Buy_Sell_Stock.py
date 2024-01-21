'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

'''
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

'''

from typing import List

class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        min_profit = float('inf')
        max_profit = 0 
        for i in range(len(prices)):
            if prices[i] < min_profit:
                min_profit = prices[i] 
            temp_values = prices[i] - min_profit
            if temp_values >= max_profit:
                max_profit = temp_values 
        return max_profit
    
    def maxProfit2(self, prices: List[int]) -> int:
        min_profit = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_profit:
                min_profit = price
            max_profit = max(max_profit, price - min_profit)
        return max_profit

if __name__ == "__main__":
    print(Solution().maxProfit1([7,1,5,3,6,4]))
    print(Solution().maxProfit2([7,1,5,3,6,4]))