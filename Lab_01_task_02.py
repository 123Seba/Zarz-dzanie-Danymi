import json

def wczytaj_dane(nazwa_pliku):
    """Funkcja do wczytywania danych z pliku JSON."""
    try:
        with open(nazwa_pliku) as plik:
            dane = json.load(plik)
    except FileNotFoundError:
        print(f'Plik "{nazwa_pliku}" nie istnieje. Utworzono nowy plik.')
        dane = {}
    return dane

def zapisz_dane(dane, nazwa_pliku):
    """Funkcja do zapisywania danych do pliku JSON."""
    with open(nazwa_pliku, 'w') as plik:
        json.dump(dane, plik, indent=4)

def wyswietl_definicje(dane):
    """Funkcja do wyświetlania definicji słów."""
    print('Definicje słów:')
    for slowo, definicja in dane.items():
        print(f'{slowo}: {definicja}')

def dodaj_definicje(dane):
    """Funkcja do dodawania nowych definicji."""
    slowo = input('Podaj słowo: ')
    definicja = input('Podaj definicję słowa: ')
    dane[slowo] = definicja
    print(f'Dodano definicję słowa "{slowo}".')

def usun_definicje(dane):
    """Funkcja do usuwania definicji słów."""
    slowo = input('Podaj słowo do usunięcia: ')
    if slowo in dane:
        del dane[slowo]
        print(f'Usunięto definicję słowa "{slowo}".')
    else:
        print(f'Słowo "{slowo}" nie istnieje w danych.')

def main():
    """Główna funkcja programu."""
    nazwa_pliku = 'data.json'
    dane = wczytaj_dane(nazwa_pliku)

    while True:
        print('\nCo chcesz zrobić?')
        print('1. Wyświetl definicje słów')
        print('2. Dodaj nową definicję słowa')
        print('3. Usuń definicję słowa')
        print('4. Zakończ program')
        wybor = input('Wybierz opcję (1/2/3/4): ')

        if wybor == '1':
            wyswietl_definicje(dane)
        elif wybor == '2':
            dodaj_definicje(dane)
        elif wybor == '3':
            usun_definicje(dane)
        elif wybor == '4':
            zapisz_dane(dane, nazwa_pliku)
            print('Zapisano zmiany. Do widzenia!')
            break
        else:
            print('Nieprawidłowa opcja. Spróbuj ponownie.')

if __name__ == "__main__":
    main()
