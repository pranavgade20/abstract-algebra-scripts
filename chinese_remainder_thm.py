from functools import reduce


def inverse(num, mod):
    for i in range(1, mod):
        if (i * num) % mod == 1:
            return i
    return mod


def main():
    Ns = [3, 5, 7]
    As = [2, 3, 2]

    n = reduce(lambda x, y: x * y, Ns)
    print(sum((As[i] * (n // Ns[i]) * inverse((n // Ns[i]), Ns[i]) for i in range(len(Ns)))) % n)


if __name__ == '__main__':
    main()
