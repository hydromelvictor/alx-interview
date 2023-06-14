#!/usr/bin/python3
""" making change """


def makeChange(coins, total):
    """
    description
    ===========
    Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total.

    parameters
    ==========
    coins
    total

    __return__ : int
    """
    sum, i = 0, 0
    if total <= 0:
        return 0
    coins = [i for i in sorted(coins, reverse=True) if i <= total]
    if len(coins) == 0:
        return -1
    for one in coins:
        if sum == total:
            return i
        if (sum + one) == total:
            return i + 1
        if (sum + one) > total:
            continue
        while sum < total:
            if (sum + one) > total:
                break
            sum += one
            i += 1
    if sum == total:
        return i
    return -1
