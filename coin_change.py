def greedy_coin_change(denominations, amount):
    coin_count = [0] * len(denominations)

    for i in range(len(denominations) - 1, -1, -1):
        while amount >= denominations[i]:
            amount -= denominations[i]
            coin_count[i] += 1

    return coin_count

def main():
    denominations = [1, 5, 10, 25]  # Coin denominations (e.g., pennies, nickels, dimes, quarters)
    amount = int(input("Enter the amount for which you want to make change: "))

    coin_count = greedy_coin_change(denominations, amount)

    print("Minimum number of coins needed:")
    for i in range(len(denominations)):
        if coin_count[i] > 0:
            print(f"{coin_count[i]} coin(s) of denomination {denominations[i]}")

if __name__ == "__main__":
    main()
