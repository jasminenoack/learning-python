
def best_change(amount, coins):
    if amount == 0:
        return []
    current_change = []

    for idx, coin in enumerate(coins):
        change = []

        if coin == 1:
            change = [coin] * amount
            new_amount = 0
            new_coins = coins
        elif amount >= coin:
            new_coins = coins[idx:]
            new_amount = amount - coin
            change = [coin] + best_change(new_amount, new_coins)
        else:
            continue

        if (current_change and len(change) < len(current_change)) or (not current_change):
            current_change = change

    return current_change

print best_change(14, [10, 7, 1])
print best_change(56, [10, 7, 1])
print best_change(39, [10, 7, 1])
print best_change(140, [10, 7, 1])
print best_change(567, [10, 7, 1])
print best_change(1050, [10, 7, 1])
print best_change(5456, [10,7,1])