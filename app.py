from dataclasses import dataclass
import json

@dataclass
class Produkt:
    nazwa: str
    cena: float
    kategoria: str
    ilosc: int

magazyn = [Produkt("mleko", 4.5, "spozywczy", 5), Produkt("sól", 2.5, "przyprawa", 0)]

with open("magazyn.json", "w", encoding="utf-8") as f:
    json.dump([p.__dict__ for p in magazyn], f, ensure_ascii=False, indent=4)
print("zapisano do pliku\n")

def wyswietl(p, prefiks="Nazwa"):
    print(f"{prefiks}: {p.nazwa}, Kategoria: {p.kategoria}, Cena: {p.cena} zł, Sztuk: {p.ilosc}")

menu = ("--- MENU ---\n1 - Wszystkie produkty\n2 - Dostępne produkty\n"
        "3 - Wyszukaj produkt\n4 - Produkty do podanej ceny\n"
        "5 - Kup produkt\n0 - Zakończ program")

while True:
    print(menu)
    wybor = input("Wybierz opcję: ").strip()
    
    if wybor == "1":
        print("--- WSZYSTKIE PRODUKTY ---")
        for p in magazyn: wyswietl(p)

    elif wybor == "2":
        print("--- DOSTĘPNE PRODUKTY ---")
        for p in [p for p in magazyn if p.ilosc > 0]: wyswietl(p)

    elif wybor == "3":
        fraza = input("Podaj nazwę produktu: ").strip().lower()
        trafienia = [p for p in magazyn if p.nazwa.lower() == fraza]
        [wyswietl(p, "Znaleziono") for p in trafienia] or print("Nie znaleziono produktu.")

    elif wybor == "4":
        try:
            limit = float(input("Podaj maksymalną cenę: "))
            print(f"--- PRODUKTY DO {limit} zł ---")
            for p in [p for p in magazyn if p.cena <= limit]: wyswietl(p)
        except ValueError:
            print("Podano nieprawidłową cenę")

    elif wybor == "5":
        szukany = input("Podaj produkt: ").strip().lower()
        for p in magazyn:
            if p.nazwa.lower() == szukany:
                print("Produkt niedostępny" if p.ilosc == 0 else f"Kupiono {p.nazwa}\nPozostało sztuk: {p.ilosc}")
                if p.ilosc > 0: p.ilosc -= 1
                break
        else:
            print("Nie znaleziono produktu")

    elif wybor == "0":
        print("Zakończono program")
        break

    else:
        print("Wybierz cyfrę od 0 do 5")
        
    print()
