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


def main():
    print("Witaj w grze Abelowy Thue Online")
    k = int(input("Podaj liczbę liter alfabetu: "))
    n = int(input("Podaj maksymalną długość ciągu: "))

    if k <= 0 or n <= 0:
        print("Złe wartości liczbowe")
        exit()

    A = [i for i in range(1, k + 1)]  # alfabet od 1 do k
    print("To jest twój alfabet :", A)

    s = int(input("Jaką strategię wybierasz? Wpisz: 1 (losowa) lub  2 (trudna): "))
    while s not in [1, 2]:
        s = int(input("Błedny wybór! Jaką strategię wybierasz? Wpisz: 1 (losowa) lub  2 (trudna): "))

    if s == 2:
        print("Wybrano strategię trudna")
        if k <= 6:
            l = int(k / 2) if k % 2 == 0 else int((k + 1) / 2)
            P = [i for i in range(1, l + 1)]
            ans = int(input("Podaj wybraną literę z alfabetu: "))

            while ans not in A:
                ans = int(input("Podałeś błędną literę! Podaj wybraną literę z alfabetu: "))

            result = [ans]
            print("Aktualny ciąg: ", result)
            place = 1

            while len(result) < n:
                if ans in P:
                    place += 1

                wyswietlenie = list(result)
                wyswietlenie.insert(place-1, '_')
                print(f"Na miejscu {place} : {wyswietlenie} podaj wybraną literę z alfabetu:")
                ans = int(input())

                while ans not in A:
                    print("Podałeś błędną literę! Podaj wybraną literę z alfabetu: ")
                    ans = int(input())

                result.insert(place - 1, ans)
                print("Aktualny ciąg:", result)
                if sprawdz_abel(result, A)[0] == 1:
                    print("Przegrałeś!")
                    print(f'Repetycja to: {sprawdz_abel(result, A)[1]}')
                    exit()
        else:
            ans = int(input("Podaj wybraną literę z alfabetu: "))
            while ans not in A:
                print("Podałeś błędną literę! Podaj wybraną literę z alfabetu: ")
                ans = int(input())
            result = [ans]
            print("Aktualny ciąg: ", result)

            while len(result) < n:
                count = [0 for i in
                         range(1, len(result) + 2)]  # lista do której zapisuje, ile liczb na danym miejscu da nam repetycje
                for place in range(1, len(result) + 2):
                    for element in A:
                        result2 = list(result)
                        result2.insert(place - 1, element)
                        if sprawdz_abel(result2, A)[0] == 1:  # jesli jest repetycja
                            count[place - 1] += 1
                        if count[place - 1] == k:  # jeśli na którymś miejscu będzie liczba równa liczbie liter alfabetu
                            wyswietlenie = list(result)
                            wyswietlenie.insert(place - 1, '_')
                            print(f"Na miejscu {place}: {wyswietlenie} podaj wybraną literę z alfabetu:")
                            ans = int(input())

                            while ans not in A:
                                print("Podałeś błędną literę! Podaj wybraną literę z alfabetu: ")
                                ans = int(input())

                            result.insert(place - 1, ans)
                            print("Aktualny ciąg:", result)
                            print("Przegrałeś!")
                            print(f'Repetycja to: {sprawdz_abel(result, A)[1]}')
                            exit()
                #print(count)
                #max_value = max(count)  # największa wartość
                l = len(count)
                list_ind = []

                for i in range(0, l):
                    if count[i] == max(count):
                        list_ind.insert(0, i)
                place = random.choice(list_ind)

                #place = count.index(max_value)  # pierwszy indeks gdzie mamy największą wartość

                wyswietlenie = list(result)
                wyswietlenie.insert(place, '_')
                print(f"Na miejscu {place + 1}: {wyswietlenie} podaj wybraną literę z alfabetu:")
                ans = int(input())

                while ans not in A:
                    print("Podałeś błędną literę! Podaj wybraną literę z alfabetu: ")
                    ans = int(input())

                result.insert(place, ans)
                print("Aktualny ciąg:", result)
                if sprawdz_abel(result, A)[0] == 1:
                    print("Przegrałeś!")
                    print(f'Repetycja to: {sprawdz_abel(result,A)[1]}')
                    exit()

        print("Wygrałeś!")

    if s == 1:
        print('Wybrano strategię losową')
        ans = int(input("Podaj wybraną literę z alfabetu: "))
        while ans not in A:
            ans = int(input("Podałeś błędną literę! Podaj wybraną literę z alfabetu: "))
        result = [ans]
        print("Aktualny ciąg: ", result)

        while len(result) < n:
            place = random.randint(1, len(result)+1)
            wyswietlenie = list(result)
            wyswietlenie.insert(place - 1, '_')
            print(f"Na miejscu {place} : {wyswietlenie} podaj wybraną literę z alfabetu:")
            ans = int(input())
            while ans not in A:
                ans = int(input("Podałeś błędną literę! Podaj wybraną literę z alfabetu: "))
            result.insert(place - 1, ans)
            print("Aktualny ciąg:", result)
            if sprawdz_abel(result, A)[0] == 1:
                print("Przegrałeś!")
                print(f'Repetycja to: {sprawdz_abel(result, A)[1]}')
                exit()
    print("Wygrałeś!")

if __name__ == "__main__":
    main()
