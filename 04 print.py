# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#liczymy pole koła

WartoscPi = 3.14
PromienOkregu = 5
PoleKola = WartoscPi * PromienOkregu ** 2
print(PoleKola)

#Kwadrat
BokKwadrat = 12.15
WynikK = BokKwadrat * BokKwadrat
ObwodK = BokKwadrat * 4
print(WynikK)
print(ObwodK)

#prostokat
BokA = 7.123
BokB = 16.516
WynikP = BokA * BokA
ObwodP = 2 * BokA + 2 * BokB
print(WynikP)
print('Wynik = ' , ObwodP)

print(1,2,3, sep="\n") # sep = "\n" każda wartosc w osobnej lini
print(1,2,3, sep="\t") # sep = "\t" każda wartosc oddzielona tabulatorem
print("this is bell: \a") # \a wywołanie domylnego dzwięku z systemu
print("\u03A3") #wyswietlanie kodów aski (unicode)
print("backslesh wyswietlony dwa razy: \\") # należy wpisać \\ dwa razy

print("TVP1", "TVP2", "TVN", "Polsat", "BBC", "HBO", "MTV" , sep = "; ")





print('I like computers ', 'TVP1', 'TVP2', 'TVN', 'Polsat', 'BBC', 'HBO', sep= 'but better is ')

print('I like computers ','TVP1','TVP2','TVN','Polsat','BBC','HBO','MTV', sep=' but better is ')

























