def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    change = 1
    
    for coin in coins:
        if coin > change:
            return change
        change +=  coin
        print(f"Change: {change - coin}", f"Coin: {coin}", f"Change + coin: {change}", sep="\n")
    
    return change

if __name__ == "__main__":
    nonConstructibleChange([5, 7, 1, 1, 2, 3, 22])