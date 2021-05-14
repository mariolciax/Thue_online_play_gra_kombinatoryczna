import random


def sprawdz_abelowo(slowo, alfabet):
    """
    Sprawdzanie repetycji abelowych juz w konkretnych podslowach.
    :param list slowo: slowo do sprawdzenia pod wzgledem repetycji abelowych
    :param list alfabet: alfabet
    :return: liczba (0- brak repetycji abelowych, 1- slowo ma repetycje abelowa)
    """
    n = len(slowo)
    p = n // 2
    a = len(alfabet)
    wystapienia_1 = [0 * i for i in range(0, a)]
    wystapienia_2 = [0 * i for i in range(0, a)]
    for i in range(0, a):
        for j in range(0, p):
            if slowo[j] == alfabet[i]:
                wystapienia_1[i] = wystapienia_1[i] + 1
        for k in range(p, n):
            if slowo[k] == alfabet[i]:
                wystapienia_2[i] = wystapienia_2[i] + 1
    for g in range(0, a):
        if wystapienia_1[g] != wystapienia_2[g]:
            return 0
    return 1


def sprawdz_abel(slowo, alfabet):
    """
    Przeszukiwanie calego slowa pod wzgledem repetycji abelowych.
    :param slowo: slowo do sprawdzenia
    :param alfabet: alfabet
    :return: lista zawierajaca na pierwszej pozycji numer (0-brak repetycji, 1-wystepuje repetycja), a na drugiej wartość (0 lub slowo z zaznaczona repetycja)
    """
    n = len(slowo)
    m = n // 2
    for k in range(1, m + 1):
        w = n - 1 - 2 * (k - 1)  # liczba podslow dlugosci k do sprawdzenia
        for j in range(0, w):
            if sprawdz_abelowo(slowo[j:j + 2 * k], alfabet) == 1:
                repetycja = slowo
                repetycja.insert(j, '<')
                repetycja.insert(j + k + 1, '-')
                repetycja.insert(j + 2 * k + 2, '>')
                s = ''
                for c in repetycja:
                    s += str(c)
                return [1, s]
    return [0, 0]


def alfabet(k):
    """
    Funkcja generująca alfabet od 1 do k.
    :param k:  długość alfabetu
    :return: alfabet
    """
    return list(range(1, k + 1))


def wybierz_strategie():
    """
    Funkcja pozwala wybrać rodzaj strategii
    :return: numer strategii (1 (losowa) lub  2 (trudna))
    """
    s = int(input("Jaką strategię wybierasz? Wpisz: 1 (losowa) lub  2 (trudna): "))
    while s not in [1, 2]:
        s = int(input("Błedny wybór! Jaką strategię wybierasz? Wpisz: 1 (losowa) lub  2 (trudna): "))
    return s


def pobierz_litere(A):
    """
    Funkcja pobiera litere od użytkownika
    :param A: alfabet
    :return: pobrana litera
    """
    litera = int(input("Podaj wybraną literę z alfabetu: "))
    while litera not in A:
        litera = int(input("Podałeś/Podałaś błędną literę! Podaj wybraną literę z alfabetu: "))
    return litera


def strategia_1(A, n):
    """
    :param list A: alfabet
    :param int n: maksymalna długość ciągu
    :return: list
    """
    litera = pobierz_litere(A)
    result = [litera]
    print("Aktualny ciąg: ", result)
    while len(result) < n:
        place = random.randint(1, len(result) + 1)
        result.insert(place - 1, '_')
        print(f"Na miejscu {place} : {result} ")
        litera = pobierz_litere(A)
        result[place - 1] = litera
        print("Aktualny ciąg:", result)
        if sprawdz_abel(result, A)[0] == 1:
            przegrana(result, A)
            return
    wygrana()


def strategia_2a(A, n):
    """
    Strategia dla k<=6
    :param int n: dlugosc ciagu
    :param int k: liczba liter alfabetu
    :return: ciąg
    """
    k = len(A)
    l = k // 2 if k % 2 == 0 else (k + 1) // 2
    P = [i for i in range(1, l + 1)]
    litera = pobierz_litere(A)
    result = [litera]
    print("Aktualny ciąg: ", result)
    place = 1

    while len(result) < n:
        if litera in P:
            place += 1

        result.insert(place - 1, '_')
        print(f"Na miejscu {place} : {result} ")
        litera = pobierz_litere(A)
        result[place - 1] = litera
        print("Aktualny ciąg:", result)
        if sprawdz_abel(result, A)[0] == 1:
            przegrana(result, A)
            return
    wygrana()


def najlepsze_miejsce(count):
    """
    Znajduje numery indeksów miejsc, w których jest największa ilość możliwości repetycji
    :param list count: Lista z wartościami określającymi ile liter da repetycje na danym miejscu
    :return list: lista indeksów
    """
    list_ind = []
    for i in range(0, len(count)):
        if count[i] == max(count):
            list_ind.insert(0, i)
    return list_ind


def list_repetycje(result, k):
    """
    Funkcja generuje liste składającą się z wartości mówiących ile liczb na danym miejscu da nam repetycje
    :param list result: utworzony ciag
    :param int k: długość alfabetu
    :return list: lista
    """
    A = alfabet(k)
    count = [0 for _ in
             range(1, len(result) + 2)]  # lista do której zapisuje, ile liczb na danym miejscu da nam repetycje
    for place in range(1, len(result) + 2):
        for element in A:
            result2 = list(result)
            result2.insert(place - 1, element)
            if sprawdz_abel(result2, A)[0] == 1:  # jesli jest repetycja
                count[place - 1] += 1
            if count[place - 1] == k:  # jeśli na którymś miejscu będzie liczba równa liczbie liter alfabetu
                return count
    return count


def strategia_2b(A, n):
    """
    Strategia trudna dla k>6
    :param int n:  dlugosc ciagu
    :param int k: liczba liter alfabetu
    :return list: lista
    """
    litera = pobierz_litere(A)
    result = [litera]
    print("Aktualny ciąg: ", result)
    while len(result) < n:
        count = list_repetycje(result, len(A))
        place = random.choice(najlepsze_miejsce(count))
        result.insert(place, '_')
        print(f"Na miejscu {place + 1}: {result} ")
        litera = pobierz_litere(A)
        result[place] = litera
        print("Aktualny ciąg:", result)
        if sprawdz_abel(result, A)[0] == 1:
            przegrana(result, A)
            return
    wygrana()


def strategia_2(A, n):
    """
    Wybiera odpowiedni wariant strategii 2
    :param int n: dlugosc ciagu
    :param int k: długosc alfabetu
    :return list: ciag
    """
    if len(A) <= 6:
        strategia_2a(A, n)
    else:
        strategia_2b(A, n)


def przegrana(result, A):
    print("Przegrałeś/Przegrałaś!")
    print(f'Repetycja to: {sprawdz_abel(result, A)[1]}')


def wygrana():
    print("Wygrałeś/Wygrałaś!")


def pobierz_wartosci():
    """
    Funkcja pobiera wartości od użytkownika
    :return: k, n liczba liter alfabetu, maksymalna dlugosc ciagu
    """
    k = int(input("Podaj liczbę liter alfabetu: "))
    n = int(input("Podaj maksymalną długość ciągu: "))
    while k <= 0 or n <= 0:
        print("Złe wartości liczbowe")
        k = int(input("Podaj liczbę liter alfabetu: "))
        n = int(input("Podaj maksymalną długość ciągu: "))
    return k, n


def main():
    print("Witaj w grze Abelowy Thue Online")
    k, n = pobierz_wartosci()
    A = alfabet(k)
    print("To jest twój alfabet: ", A)
    s = wybierz_strategie()
    if s == 1:
        print('Wybrano strategię losową')
        strategia_1(A, n)
    elif s == 2:
        print("Wybrano strategię trudną")
        strategia_2(A, n)


if __name__ == '__main__':
    main()


