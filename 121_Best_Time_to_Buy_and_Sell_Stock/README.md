# 121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Intuition
To maximize profit, we need to find the maximum difference between a buying price and a selling price where the selling day is after the buying day. We can track the minimum price seen so far and calculate the profit for each potential selling day.

## Approach
Initialize min_price to a large number and max_profit to 0.
Iterate through the prices:
- Update min_price if the current price is lower.
- Otherwise, calculate the profit (current price - min_price) and update max_profit if it's higher.
This ensures we always buy at the lowest price before selling.

## Complexity
- Time complexity: O(n), where n is the number of days, as we traverse the array once.
- Space complexity: O(1), using only a few variables.

## Code
```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
```

## Examples
- Input: prices = [7,1,5,3,6,4]  
  Output: 5  
  Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 5.

- Input: prices = [7,6,4,3,1]  
  Output: 0  
  Explanation: No profit possible, so return 0.