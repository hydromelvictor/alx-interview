#!/usr/bin/python3
"""
prime game
"""


def isprime(p):
    """ prime number """
    if p == 0 or p == 1:
        return False
    if p == 2:
        return True
    else:
        for i in range(2, p - 1):
            if i % p == 0:
                return False
        return True


def isWinner(x, nums):
    """ winner
        maria est pair
        ben est impair
    """
    i = 0
    ens = None
    for tr in range(x):
        ens = list(range(1, nums[tr] + 1))
        for _ in range(len(ens)):
            n = 0
            res = None
            for s in ens:
                if isprime(s):
                    n = s
                    break
            if n:
                res = ens[:]
                res.remove(n)
                for k in ens:
                    if k % n == 0 and k in res:
                        res.remove(k)
                ens = res[:]
                i += 1
    #if len(ens) != 0:
    if 2 % i == 0:
        return 'Maria'
    else:
        return 'Ben'
    return None
