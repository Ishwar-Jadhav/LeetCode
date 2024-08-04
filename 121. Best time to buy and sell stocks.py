prices = [1,2,4,2,5,7,2,4,9,0,9]
#Output: 9

l, r = 0, 1
maxProfit = 0

while r < len(prices):
    if prices[l] < prices[r]:
        profit = prices[r] - prices[l]
        maxProfit = max(maxProfit, profit)
    else:
        l += r
    r += 1
print(maxProfit)