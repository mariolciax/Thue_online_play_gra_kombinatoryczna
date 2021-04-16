print("Witaj w grze Abelowy Thue Online")
k= int(input("Podaj liczbę liter alfabetu: "))
n = int(input("Podaj maksymalną długość ciągu: "))
A = [ i for i in range(1,k+1)]  #alfabet od 1 do k
print("To jest twój alfabet :", A)
if k <= 6:
    if k % 2 == 0:  #tworze podciągi P D
        l = int(k/2)  #długość podciągu
        P = [i for i in range(1,l+1)]
        D = [i+l for i in range(1,l+1)]
        #print(P)
        #print(D)
    else:
        l1 = int((k+1)/2)
        l2 = int((k-1)/2)
        P = [i for i in range(1,l1+1)]
        D = [i+l1  for i in range(1,l2+1)]
        print(P)
        print(D)

    ans = int(input("Podaj wybraną literę z alfabetu: "))
    result = []
    result.insert(0, ans)
    print(result)
    place = 1
    
    while len(result)<n:

            if ans in P:
                place = place + 1
          

            print("Na miejscu", place, "podaj wybraną literę z alfabetu:")
            ans = int(input())
            result.insert(place-1, ans)
            print("Aktualny ciąg:", result)


print("Wygrałeś!")

