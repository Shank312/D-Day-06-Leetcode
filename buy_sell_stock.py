
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')                   # start with a very high value
        max_profit = 0                             # initially, no profit
        for p in prices:
            min_price = min(min_price, p)          # update min price so far
            max_profit = max(max_profit, p - min_price)     # Calculate the profit
        return max_profit
    

# Example usage
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]                    # stock prices on each day
    solution = Solution() 
    result = solution.maxProfit(prices)
    print("Stock Prices: ", prices)
    print("Maximum Profit: ", result)

# (buy at 1, sell at 6 → profit = 5)