def wisielec():

    punktacja = 10
    haslo = ""
    literki = []

    haslo = input("Podaj hasło: ")
    podpowiedz = input("Podaj podpowiedź: ")

    print("\n"*25)

    print("Zgadnij hasło:")
    print("_" * len(haslo))
    print("Podpowiedź: ", podpowiedz)

    while punktacja != 0:
        proba = input("Zgaduję: ").lower()
        if len(proba) > 1:
            if haslo.lower() == proba:
                print("Zgadłeś!")
                break
            else:
                punktacja = punktacja - 1
                print("Nie zgadles hasła. Próbuj dalej. Twoja punktacja: ",punktacja,".")
        else:
            if haslo.lower().count(proba) > 0:
                literki.append(proba)
                for i in haslo:
                    if i in literki:
                        print(i, end="")
                    else:
                        print("_",end="")
                print("\n")
            else:
                punktacja = punktacja - 1
                print("Nie ma takiej litery. Twoja punktacja: ", punktacja,".")

    if punktacja == 0:
        print("Przegrałeś!")

if __name__ == "__main__":
    wisielec()