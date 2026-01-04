# 122. Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.

## Intuition
Since we can buy and sell multiple times, we should capture every upward trend in the stock prices. The maximum profit is the sum of all positive differences between consecutive days.

## Approach
Initialize profit to 0.
Iterate through the prices from the second day to the end.
If the current price is higher than the previous day's price, add the difference to profit.
This accumulates all possible profits from buying low and selling high on consecutive days.

## Complexity
- Time complexity: O(n), where n is the number of days, as we traverse the array once.
- Space complexity: O(1), using only a single variable.

## Code
```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
```

## Examples
- Input: prices = [7,1,5,3,6,4]  
  Output: 7  
  Explanation: Buy on day 2 (1), sell on day 3 (5), profit 4; buy on day 4 (3), sell on day 5 (6), profit 3; total 7.

- Input: prices = [1,2,3,4,5]  
  Output: 4  
  Explanation: Buy on day 1 (1), sell on day 5 (5), profit 4.

- Input: prices = [7,6,4,3,1]  
  Output: 0  
  Explanation: No increasing sequences, so profit 0.