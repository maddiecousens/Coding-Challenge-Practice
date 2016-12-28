# Author: Maddie Cousens
# From: Written for Hacker Rank 30 Days of Code

# Question: output the max # of toys give money, from list of prices of toys

def max_toys(prices, money):
    #possible = [item for item in prices if item < money]
    prices = sorted(prices)
    items_purchased = 0
    cost_tally = 0
    for price in prices:
        if cost_tally + price > money:
            return items_purchased
        else:
            cost_tally += price
            items_purchased += 1
    return items_purchased