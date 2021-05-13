# finds cycles of group (Z_n,.)

def main():
    n = 26
    l = [1] + list(filter(lambda x: n % x != 0, range(1, n)))
    d = {}
    res = {}
    for i in l:
        d[i] = False
        res[i] = []

    for i in l:
        for c in l:
            d[c] = False

        d[i] = True
        ptr = i * i
        ptr %= n
        while ptr != i:
            d[ptr] = True
            ptr = ptr * i
            ptr %= n

        for k in d:
            if d[k]:
                res[i].append(k)

    for k in res:
        print(f"{k} : {len(res[k])} => {res[k]}")


if __name__ == '__main__':
    main()
