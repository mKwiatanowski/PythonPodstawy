# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 22:00:26 2023

@author: mateu
"""

s = "A Python script"

# string tablica znaków. Podczas wyswietlania zmienna[x:z] gdzie x i z odpowiada znakowi licząc od 0
# [:z] oznacza wszystkie znaki od poczatku do znaku z
# [x:] oznacza od znaku x do końca
print(s[0])
print(s[2])
print(s[2:7])
print(s[2:8])
print(s[:8])
print(s[8:])
print(s[:8],s[8:])

# wyszukanie na której pozycji znajduje sie :
message = 'Document "cv.doc" was printed on printed: XEROX'
print(message.find(':'))

# zakladajac ze komunikat zawsze wyglada podobnie i nazwa drukarki jest po : i spacji to znajdujemy znak : i wyswietlamy
# wszystko do znajduje sie po nim [message.find(':')+2:]
print(message[message.find(':')+2:])

# wydobycie nazwy dokumenty
print(message[message.find('"')+1:]) 

# przypisac otrzymany wynik do zmiennej po czym wyszukac po raz kolejny znak "
# efektem tego jest wycieta nazwa pliku w ciagu znakow
tmp = message[message.find('"')+1:]
print(tmp[:tmp.find('"')])




















