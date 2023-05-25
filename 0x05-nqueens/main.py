def diagLeftBottom(pos, n):
    line = []
    p, q = pos
    while p < (n - 1) or q > 0:
        line.append(p)
        line.append(q)
        p += 1
        q -= 1
    return line


def diagLeftTop(pos, n):
    line = []
    p, q = pos
    while p > 0 or q > 0:
        line.append(p)
        line.append(q)
        p -= 1
        q -= 1
    return line


def diagRigthBottom(pos, n):
    line = []
    p, q = pos
    while p < (n - 1) or q < (n - 1):
        line.append(p)
        line.append(q)
        p += 1
        q += 1
    return line


def diagRigthTop(pos, n):
    line = []
    p, q = pos
    while p > 0 or q < (n - 1):
        line.append(p)
        line.append(q)
        p -= 1
        q += 1
    return line


def nqueens(n):
    ech = [[i, j] for i in range(n) for j in range(n)]
    tr = 0
    # boucle parcours n fois
    res = []
    while tr < n:
        line = []
        bad = []
        for pos in ech:
            s = 0
            for k in res:
                if pos in k:
                    s = 1
                    break
            if s != 0:
                continue
            p, q = pos
            if pos not in line and p not in bad and q not in bad:
                line.append(pos)
                bad.extend(diagLeftTop(pos, n))
                bad.extend(diagLeftBottom(pos, n))
                bad.extend(diagRigthTop(pos, n))
                bad.extend(diagRigthBottom(pos, n))
        if len(line) == n:
            res.append(line)
            print(line)
        tr += 1


if __name__ == '__main__':
    nqueens(4)
