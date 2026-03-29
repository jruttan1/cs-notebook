from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Given a list of stock prices where prices[i] is the price on day i,
        return the maximum profit you can achieve by choosing a single day
        to buy and a later day to sell. If no profit is possible, return 0.
        """
        if not prices:
            return 0

        left = 0   # buy pointer
        right = 1  # sell pointer
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                # profit can be made
                profit = prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit
            else:
                # found new lower buy price
                left = right
            right += 1

        return max_profit
    #this solution works by checking if the current buy is the current minimum and switching each time
    #it sees a new minimum. the testing the profit against the sell day to find maximum

'''
This solution was difficult as my intro to sliding window, i struggled understand the best way to store the maximum and minimum values. i should have stepped back and framed the problem as finding an i < j to maximizes prices[j]-prices[i]. I also tried to manually code a way to calculate max when python has a built in method for it.
'''