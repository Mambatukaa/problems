# Time Complexity: O(n)
# Space Complexity: O(1)
def maxProfit(prices):

    maxP = 0

    l = 0
    r = 1

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r

        r += 1

    return maxP

prices = [7, 1, 5, 3, 6, 4]
print("res:", maxProfit(prices))

""" Two pointers


L = Buy
R = Sell


"""

