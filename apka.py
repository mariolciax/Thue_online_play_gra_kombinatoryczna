
import random

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
    m = int(n / 2)
    for k in range(1, m + 1):
        w = n - 1 - 2 * (k - 1)  # liczba podslow dlugosci k do sprawdzenia
        for j in range(0, w):
            if sprawdz_abelowo(slowo[j:j + 2 * k], alfabet) == 1:
                repetycja = slowo
                repetycja.insert(j, '<')
                repetycja.insert(j + k + 1, '-')
                repetycja.insert(j + 2 * k + 2, '>')
                s=''
                for c in repetycja:
                    s += str(c)
                return [1, s]
    return [0, 0]

def alfabet(k):
    """
    Funkcja generująca alfabet
    :param k:  długość alfabetu
    :return: alfabet
    """
    A = [i for i in range(1, k + 1)]  # alfabet od 1 do k
    return A


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
    ans= int(input("Podaj wybraną literę z alfabetu: "))
    while ans not in A:
        ans = int(input("Podałeś błędną literę! Podaj wybraną literę z alfabetu: "))
    return ans

def strategia_1(A, n):
    """
    :param list A: alfabet
    :param int n: maksymalna długość ciągu
    :return: none
    """
    ans = pobierz_litere(A)
    result = [ans]
    print("Aktualny ciąg: ", result)
    while len(result) < n:
        place = random.randint(1, len(result) + 1)
        wyswietlenie = list(result)
        wyswietlenie.insert(place - 1, '_')
        print(f"Na miejscu {place} : {wyswietlenie} ")
        ans = pobierz_litere(A)
        result.insert(place - 1, ans)
        print("Aktualny ciąg:", result)
        if sprawdz_abel(result, A)[0] == 1:
            return result
    return result


def strategia_2a(n, k):
    """
    Strategia dla k<=6
    :param int n: dlugosc ciagu
    :param int k: liczba liter alfabetu
    :return: ciąg
    """
    A = alfabet(k)
    l = int(k / 2) if k % 2 == 0 else int((k + 1) / 2)
    P = [i for i in range(1, l + 1)]
    ans = pobierz_litere(A)
    result = [ans]
    print("Aktualny ciąg: ", result)
    place = 1

    while len(result) < n:
        if ans in P:
            place += 1

        wyswietlenie = list(result)
        wyswietlenie.insert(place - 1, '_')
        print(f"Na miejscu {place} : {wyswietlenie} ")
        ans = pobierz_litere(A)
        result.insert(place - 1, ans)
        print("Aktualny ciąg:", result)
        if sprawdz_abel(result, A)[0] == 1:
            return result
    return result

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
    count = [0 for i in range(1, len(result) + 2)]  # lista do której zapisuje, ile liczb na danym miejscu da nam repetycje
    for place in range(1, len(result) + 2):
        for element in A:
            result2 = list(result)
            result2.insert(place - 1, element)
            if sprawdz_abel(result2, A)[0] == 1:  # jesli jest repetycja
                count[place - 1] += 1
            if count[place - 1] == k:  # jeśli na którymś miejscu będzie liczba równa liczbie liter alfabetu
                return count
    return count

def strategia_2b(n, k):
    """
    Strategia trudna dla k>6
    :param int n:  dlugosc ciagu
    :param int k: liczba liter alfabetu
    :return list: lista
    """
    A = alfabet(k)
    ans =pobierz_litere(A)
    result = [ans]
    print("Aktualny ciąg: ", result)
    while len(result) < n:
        count = list_repetycje(result, A, k)
        place = random.choice( najlepsze_miejsce(count))
        wyswietlenie = list(result)
        wyswietlenie.insert(place, '_')
        print(f"Na miejscu {place + 1}: {wyswietlenie} ")
        ans = pobierz_litere(A)
        result.insert(place, ans)
        print("Aktualny ciąg:", result)
        if sprawdz_abel(result, A)[0] == 1:
            return result
    return result

def strategia_2(n, k):
    """
    Wybiera odpowiedni wariant strategii 2
    :param int n: dlugosc ciagu
    :param int k: długosc alfabetu
    :return list: ciag
    """
    if k <= 6:
        result = strategia_2a(n, k)
    else:
        result = strategia_2b(n, k)
    return result

def pobierz_wartosci():
    """
    Funkcja pobiera wartości od użytkownika
    :return: k, n liczba liter alfabetu, maksymalna dlugosc ciagu
    """
    k = int(input("Podaj liczbę liter alfabetu: "))
    n = int(input("Podaj maksymalną długość ciągu: "))
    while k <= 0 and n <= 0:
        print("Złe wartości liczbowe")
        k = int(input("Podaj liczbę liter alfabetu: "))
        n = int(input("Podaj maksymalną długość ciągu: "))
    return (k,n)

def main():
    print("Witaj w grze Abelowy Thue Online")
    k, n = pobierz_wartosci()
    A = alfabet(k)
    print("To jest twój alfabet :", A)
    s = wybierz_strategie()
    if s == 1:
        print('Wybrano strategię losową')
        result = strategia_1(A, n)
    elif s == 2:
        print("Wybrano strategię trudną")
        result = strategia_2(n, k)
    if s == 1 or s == 2:
        if sprawdz_abel(result, A)[0] == 1:
            print("Przegrałeś!")
            print(f'Repetycja to: {sprawdz_abel(result, A)[1]}')
            exit()
    print("Wygrałeś!")
if __name__ == '__main__':
    main()
