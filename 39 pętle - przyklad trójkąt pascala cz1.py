# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:44:00 2023

@author: mateu
"""


# wyliczenie wartosci
numbers = [1]
print(numbers)

for i in range(5):
     
    newNumbers = [1]
    position = 0
    
    
    while position < len(numbers) - 1:
        # dodać do listy liczby ktore znajduja sie na pozycji i pozycji + 1
        newNumbers.append(numbers[position] + numbers[position + 1])
        position += 1
    
    newNumbers.append(1)

    numbers = newNumbers.copy()

    print(numbers)





# konwersja liczb w tabeli na tekst
# dobra praktyka kodowania to jesli jakas liczba powtarza sie to najlepiej zadeklarowac ja jako zmienna 
# latwiej bedzie kiedys komus poprawic ten kod

numbers = [1]
windth = 100
height = 15


# petla ktora zamienia wartosci z listy numbers na tekst w zmiennej line 
line = ''
for n in numbers:
    line += " %4d " % (n)

# aby zapis zaczął wygladac jak trojkat mozna uzyc funkcji center(ilosc znakow) co sprawi ze caly wyswietlany tekst
# zostanie wycentrowany na 50 znaku
print(line.center(windth))


for i in range(height-1):
     
    newNumbers = [1]
    position = 0
    
    
    while position < len(numbers) - 1:
        # dodać do listy liczby ktore znajduja sie na pozycji i pozycji + 1
        newNumbers.append(numbers[position] + numbers[position + 1])
        position += 1
    
    newNumbers.append(1)

    numbers = newNumbers.copy()

    line = ''
    for n in numbers:
        line += " %4d " % (n)

    print(line.center(windth))



















































