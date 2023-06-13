# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 13:04:47 2023

@author: mateu
"""



line = "this IS a very STRANGE text"

# capitalize() formatowanie tekstu do formy duża litera na początku zdania i reszta z małych liter
print(line.capitalize())

# title() każde słowo zaczyna się od dużej litery
print(line.title())


# upper() wszystko duże liter
print(line.upper())

# lower() wszystko male litery
print(line.lower())

# swapcase() każdą małą litere zamienia na duża a kazda duza zamienia na mala
print(line.swapcase())

# casefold() na przykładzie j niemieckiego i slow der FluB pozwoli zamienic slowo FluB z tym dziwnym znakiem B
# na wyraz fluss to samo tylko w innym zapisie

# ta funkcja nie działa w jezyku polski i nie zamieni polskich znakow ą na a itp
line = "Łabądź"
print(line.casefold())

# można to obejsc stosujac replace() zamiane znakow
print(line.replace("Ł", "L").replace("Ą","A").replace("Ź", "Z").lower())


# count() ile razy cos wystepowało np litera w danym napisie
print(line.count("e"))

# find() sprawdzenie na której pozycji wystepuj i tak badamy od lewej
print(line.find("e"))

# rfind() sprawdzenie na której pozycji wystepuj i tak badamy od prawej
print(line.rfind("e"))



# index() podobne znaczenie co find
print(line.index("e"))

# rindex podobne zaczenie do rfind
print(line.rindex("e"))

# różnice mozna dostrzec gdy sprobujemy znalezc cos czego nie ma w tekscie gdy uzyjemy find to gdy czegos nie znajdzie
# otrzymany wynik to -1 natomiast przy uzyciu index otrzymany wynik to blad


# do badanie czy cos znajduje sie w teksie lub tez nie dobrym rozwiazaniem jest tez operator logiczny in
# otrzymamy true lub false
'e' in line

'p' in line


# obie te funkcje sa czule na wielkosc liter
# startswith() czy dany ciag znakow zaczyna sie od 
print(line.startswith("This"))

# endswith czy dany ciag znakow konczy sie na 
print(line.endswith("text"))


# zamkniecie dlugiego tekstu za pomoca potrojnego cudzyslowia """ asdfasdf asd """
line = """ this is a long text
that spans multiple line
but should be somehow presented in python """

# wszystkie znaki entera zostaly zamienione na \n
line

print(line)




# specjalistyczne operacje na teksie moga byc dostepne w innych modulach


import string

# predefiniowane stałe

string.ascii_letters

string.digits





line = "this IS a very STRANGE text"

# funkcja split() pozwala rozbic tekst na liste, trzeba w nawiasie wskazac ze wzgledu na co ma sie odbywac rozbicie
# najczesciej spacja, eneter, itp
line.split(" ")

lista = line.split(" ")
lista

# join() odwrotnosc split(), czyli z listy tworzy ciagly tekst
# aby to zadziałalo nalezy najpierw wskazac separator ktory bedzie lacznikiem np spacja " ".join(lista)
# i nastpnie w join() w nawiasie dopiero podajemy nazwe listy z ktorej ma zostac utworzony tekst
" ".join(lista)



poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! '''


lines = poem.split("\n")



for i in range(8):
    print(lines[i])
    print(lines[i+8])
    



















