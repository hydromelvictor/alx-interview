#!/usr/bin/python3
"""
Vous avez n nombre de boîtes verrouillées devant vous.
Chaque case est numérotée séquentiellement de 0 à n - 1 et
chaque case peut contenir les clés des autres cases.

Write a method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    boxes : parameters
    _return_ : boolean
    """
    res = [0]
    if len(boxes[0]) == 0:
        return False
    for i in res:
        for j in boxes[i]:
            if j <= len(boxes) - 1 and j not in res:
                res.append(j)
    if len(res) >= len(boxes):
        return True
    else:
        return False
