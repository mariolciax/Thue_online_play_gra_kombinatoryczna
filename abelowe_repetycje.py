import math


def sprawdz_abelowo(slowo, alfabet):  # sprawdzanie repetycji abelowych juz w konkretnych podslowach
    n = len(slowo)
    p = int(n / 2)
    a = len(alfabet)
    wystapienia_1 = [0 * i for i in range(0, a)]
    wystapienia_2 = [0 * i for i in range(0, a)]
    for i in range(0, a):
        for j in range(0, p):
            if slowo[j] == alfabet[i]:
                wystapienia_1[i] = wystapienia_1[i] + 1
        for k in range(p, n):
            if slowo[k] == alfabet[i]:
                wystapienia_2[i] = wystapienia_2[i] + 1  # a.count(x) liczba wystapien elementu x na liscie
    for g in range(0, a):
        if wystapienia_1[g] != wystapienia_2[g]:
            return 0
    return 1


def sprawdz_abel(slowo, alfabet):  # przeszukiwanie calego slowa pod wzgledem repetycji abelowych
    n = len(slowo)
    m = math.floor(n / 2)
    for k in range(1, m + 1):
        w = n - 1 - 2 * (k - 1)  # liczba podslow dlugosci k do sprawdzenia
        for j in range(0, w):
            if sprawdz_abelowo(slowo[j:j + 2 * k], alfabet) == 1:
                return 1
    return 0


def sprawdz(slowo, alfabet):
    if sprawdz_abel(slowo, alfabet) == 1:
        print('słowo ma repetycje abelowa')
    if sprawdz_abel(slowo, alfabet) == 0:
        print('slowo nie ma repetycji abelowych')


def main():
    sprawdz([1, 2, 3, 2, 1, 3], [1, 2, 3])  # tu mozna posprawdzac czy dobrze dziala
    sprawdz([1, 2, 3, 2, 1, 2, 3], [1, 2, 3])
    sprawdz([1, 2, 1, 2, 3, 2], [1, 2, 3])
    sprawdz([1, 2, 3, 4, 2, 3, 1, 2, 3, 2, 4, 1, 3], [1, 2, 3, 4])  # 234231 232413


if __name__ == "__main__":
    main()
