# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 11:18:26 2023

@author: mateu
"""


# range(x) pozwala wygenerowac olreslona x ilosc liczb
# jesli chcemy zeby range mialo okreslony zakres np od 1 do 20 to wykonac trzeba zapis
# range(1,21)
# range(1,21,2)  moze posiadac 3 parametr i oznacza o ile nalezy powiekszac poczatkowy wartosc zakresu
for number in range(1,21):
    
    # sprawdzenie czy liczba jest parzysta poprzez podzielenie jej modulo 2 i sprawdzimy czy wynik jest == 0
    if number %2 == 0:
        print("Numer %2d is %s " % (number,"even"))
    else:
        print("Numer %2d is %s " % (number,"odd"))
    
    #print(number)




string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'


for i in range(10):
    print(string_A)
    




for i in range(9):
    if i %2 == 0:
        print(string_A)
    else:
        print(string_B)





for i in range(1,10):
    print("x"*i)
    

for i in range(1,10):
    if i %2 == 0:
        print("o"*i)
        
    else:
        print("x"*i)








