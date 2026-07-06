def max_profit(prices):
    min_price = prices[0]
    best_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        if prices[i] - min_price > best_profit:
            best_profit = prices[i] - min_price

    return best_profit

print(max_profit([2,3,4,5,6,7]))
print(max_profit([7,1,5,3,6,4]))
print(max_profit([7, 6, 4, 3, 1]))