import itertools
import random

def main():
    # Pobieranie listy fraz od użytkownika
    frazy_input = input("Podaj frazy oddzielone przecinkami: ")
    frazy = [fraza.strip() for fraza in frazy_input.split(",")]

    # Pobieranie liczby kombinacji i liczby fraz w kombinacji od użytkownika
    ilosc_kombinacji = int(input("Podaj liczbę kombinacji: "))
    ilosc_fraz_w_kombinacji = int(input("Podaj liczbę fraz w kombinacji: "))

    # Tworzenie wszystkich możliwych kombinacji fraz
    kombinacje = []
    for _ in range(ilosc_kombinacji):
        # Losowe wybieranie fraz do kombinacji
        kombinacja = random.sample(frazy, ilosc_fraz_w_kombinacji)
        kombinacje.append(kombinacja)

    # Wyświetlanie wybranych kombinacji
    print("Wybrane kombinacje:")
    for i, kombinacja in enumerate(kombinacje, start=1):
        print(f"Alt {i}: {', '.join(kombinacja)}")

if __name__ == "__main__":
    main()
