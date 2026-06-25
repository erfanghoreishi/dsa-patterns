#121. Best Time to Buy and Sell Stock
def maxProfit(prices):
    max_profit = 0
    cheapest = prices[0]
    for price in prices:
        cheapest = min(cheapest, price)        # best buy price so far
        max_profit = max(price - cheapest, max_profit)

    return max_profit
