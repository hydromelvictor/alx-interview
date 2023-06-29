#!/usr/bin/python3
"""
prime game
"""


def isprime(p):
    """ prime number """
    if p == 0 or p == 1:
        return False

    for i in range(2, p):
        if i % p == 0:
            return False
    return True


def rm(n, rang):
    """ remove multiple"""
    for i in rang:
        if i % n == 0:
            rang.remove(i)
    return rang


def indic(rang):
    """ indic """
    i = 0
    for j in rang:
        if isprime(j):
            i += 1
            rang = rm(j, rang)
    return i


def isWinner(x, nums):
    """ winner
        maria est pair
        ben est impair
    """
    if x == 0 or nums == []:
        return None

    game = {'Maria': 0, 'Ben': 0}
    for tr in range(x):
        h = nums[x]
        rang = [s for s in range(1, h + 1)]
        ind = indic(rang)
        if ind % 2 == 0:
            game['Ben'] += 1
        elif ind % 2 != 0:
            game['Maria'] += 1
    if game['Ben'] > game['Maria']:
        return 'Ben'
    elif game['Ben'] < game['Maria']:
        return 'Maria'
    else:
        return None
