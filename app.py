import json

class Produkt:
    def __init__(self, nazwa, cena, kategoria, ilosc):
        self.nazwa = nazwa
        self.cena = float(cena)
        self.kategoria = kategoria
        self.ilosc = int(ilosc)


magazyn = [
    Produkt("mleko", 4.50, "spozywczy", 5),
    Produkt("sól", 2.50, "przyprawa", 0)
]

dane_do_zapisu = [{"nazwa": p.nazwa, "cena": p.cena, "kategoria": p.kategoria, "ilosc": p.ilosc} for p in magazyn]
with open("magazyn.json", "w", encoding="utf-8") as plik:
    json.dump(dane_do_zapisu, plik, ensure_ascii=False, indent=4)

print("zapisano do pliku")

while True:
    print("--- MENU ---")
    print("1 - Wszystkie produkty")
    print("2 - Dostępne produkty")
    print("3 - Wyszukaj produkt")
    print("4 - Produkty do podanej ceny")
    print("5 - Kup produkt")
    print("0 - Zakończ program")
    
    wybor = input("Wybierz opcję: ").strip()

    if wybor == "1":
        print("--- WSZYSTKIE PRODUKTY ---")
        [print(f"Nazwa: {p.nazwa}, Kategoria: {p.kategoria}, Cena: {p.cena} zł, Sztuk: {p.ilosc}") for p in magazyn]
        print()

    elif wybor == "2":
        print("--- DOSTĘPNE PRODUKTY ---")
        for p in magazyn:
            if p.ilosc > 0:
                print(f"Nazwa: {p.nazwa}, Kategoria: {p.kategoria}, Cena: {p.cena} zł, Sztuk: {p.ilosc}")
        print()

    elif wybor == "3":
        fraza = input("Podaj nazwę produktu: ").strip().lower()
        znaleziono = any(p.nazwa.lower() == fraza for p in magazyn)
        for p in magazyn:
            if p.nazwa.lower() == fraza:
                print(f"Znaleziono: {p.nazwa}, Kategoria: {p.kategoria}, cena: {p.cena} zł, Sztuk: {p.ilosc}")
                break
        if not znaleziono:
            print("Nie znaleziono produktu.")
        print()

    elif wybor == "4":
        try:
            limit_cenowy = float(input("Podaj maksymalną cenę: "))
            print(f"--- PRODUKTY DO {limit_ceny if 'limit_ceny' in locals() else limit_cenowy}---")
            for p in magazyn:
                if p.cena <= limit_cenowy:
                    print(f"Nazwa: {p.nazwa}, Kategoria: {p.kategoria}, Cena: {p.cena} zł, Sztuk: {p.ilosc}")
        except ValueError:
            print("Podano nieprawidłową cenę")
        print()

    elif wybor == "5":
        szukany_zakup = input("Podaj produkt: ").strip().lower()
        trafienie = False
        for p in magazyn:
            if p.nazwa.lower() == szukany_zakup:
                trafienie = True
                if p.ilosc == 0:
                    print("Produkt niedostępny")
                else:
                    p.ilosc -= 1
                    print(f"Kupiono {p.nazwa}")
                    print(f"Pozostało sztuk: {p.ilosc}")
                break
        if not trafienie:
            print("Nie znaleziono produktu")
        print()

    elif wybor == "0":
        print("Zakonczono program")
        break

    else:
        print("Wybierz cyfrę od 0 do 5")