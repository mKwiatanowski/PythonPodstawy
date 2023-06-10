# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 22:37:25 2023

@author: mateu
"""

# liste zapisujemy w nawiasie [] a wartosci oddzielamy ,
countries = ['US', 'US', 'DE', 'PL']

# indeksowanie wywolujac zmienna listowa w nawiasie [] wyswietlamy pozycje ktora chcemy uzyc

countries[1] = "GB"
print(countries[1])

# uzywajac append mozna dodac cos na koncu listy
countries.append("SP")

# aby dodac nowy element na okreslonej pozycji uzywac insert(numer pozycji, wartosc)
countries.insert(2, "IT")

# remove jesli chcemy usunac element wskazujemy jego dokladna nazwe
countries.remove('DE')

# sort() sortowanie listy
countries.sort()

# reverse() odwrocenie listy
countries.reverse()

# pop przetwazanie pokolei znajdujace sie na liscie argument to liczba ktora wskazuje
# numer elementu ktory mnie interesuje
# mozna to zastosowac jakby trzeba bylo uzyc cos jakby kolejki i przetwarzac wszystkie pozycje na liscie
# funkcja pop bedzie pobierac elementy z listy i je usuwac 
print(countries.pop(3))

# sprawdzenie na ktorej pozycji znajduje sie szukany index
print(countries.index('GB'))

# count sprawdzenie ile razy dany index znajduje sie na liscie
print(countries.count('US'))


newList = ['FI', 'SE']

# metoda extend(nowa lista)odanie nowej listy
countries.extend(newList)

# przypisanie listy do nowej listy kopia
# w takim wypadku nowa lista to taknaprawde stara lista tylko o innej nazwie ale wskazuje 
# to samo miejsce w pamieci komputera
# countriesCopy = countries

# metoda copy() aby skopiowac liste do nowej zmiennej
countriesCopy = countries.copy()

# metoda clear usuwa zawartosc listy
countriesCopy.clear()





print(countries)
print(countriesCopy)


# lista
hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']

# nowa lista
newHitsTitles = ['CHILD IN TIME' , 'AGAIN']

# dodanie nowej listy do starej listy
hitsTitles.extend(newHitsTitles)

# dodanie nowego indexu na pozycji 
hitsTitles.insert(2, "HOTEL CALIFORNIA")
hitsTitles.insert(0, "THE SOUND OF SILENCE")

# sprawdzenie numeru indexu
print(hitsTitles.index("HOTEL CALIFORNIA"))

# usuniecie indexu
hitsTitles.remove("HOTEL CALIFORNIA")

# zmiana indexu na inny
hitsTitles[0] = "ENJOY THE SILENCE"

# kopia listy
hitsToRead = hitsTitles.copy()

# odwrotna kolejnosc listy
hitsToRead.reverse()

# kolejnosc alfabetyczna
hitsToRead.sort()

# symulacja odczytania listy i usuniecie pierwszej piosenki
hitsToRead.pop(0)
hitsToRead.pop(0)

# nowa lista i dodanie jej do istniejacej listy
additionalSongs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']
hitsToRead.extend(additionalSongs)

# sprawdzenie ile razy wystepuje pozycja na liscie
print(hitsToRead.count("WISH YOU WERE HERE"))
print(hitsToRead.count("RIDERS ON THE STORM'"))

# wyczyszczenie listy
hitsToRead.clear()

print(hitsTitles)
print(hitsToRead)


































