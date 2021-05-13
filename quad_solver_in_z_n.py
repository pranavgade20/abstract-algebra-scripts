# solves quadratic eqns in ring Z_n

def main():
    # ax^2 + bx + c = 0 (in Z_n)
    a = 1
    b = -5
    c = 6
    n = 12

    for i in range(0, n):
        if (a * i * i + b * i + c) % n == 0:
            print(i)


if __name__ == '__main__':
    main()
