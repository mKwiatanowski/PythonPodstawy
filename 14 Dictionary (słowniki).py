# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 10:12:23 2023

@author: mateu
"""


# zmienna zapisana w nawiasach {} to lista wartosci
# nowe wpisy sa oddzielone miedzy soba ,
# slownik ma 2 wartosci, gdzie kluczem jest pierwszy argument 'PL'
# i wtedy wyswietlane sa wartosci przechowywane w slowniku czyli 'Duda'
CountryLeaders = {'PL':'Duda', 'US':'Trump'}

# wywolanie w slowniku po kluczu i wyswietlenie wartosci przypisanej do klucza
# print(CountryLeaders['US'])

# dodanie do slownika nowego klucza i przypisanego do niego wartosci
# po nazwie zmiennej w [ klucz ] a po = wartosc 
CountryLeaders['DE'] = 'Merkel'


# metody dostepne w slownikach 
# wyswietlenie kluczy jakie znajduja sie w slowniki
#print(CountryLeaders.keys())

# wyswietlenie wartosci jakie znajduja sie w slowniku
#print(CountryLeaders.values())

# kolekcja elementow zarowno klucz jak i wartosc
#print(CountryLeaders.items())

# przetwarzanie wszystkich elementow znajdujacych sie w slowniku  pop lub popitem
# popitem pobierze jeden z elementow dictionery zwroci go a nastepnie usunie z dectionery
# popitem to destruktywna iteracja po slowniku dzieki temu mozemy przechodzic krok po kroku 
# a nasteonie taki element jest usuwany ze slownika
# print(CountryLeaders.popitem())

# setdefault(key, value) specyficzna metoda w slownikach 
# moze byc tak ze w slowniku jeszcze nie jest zdefiniowany wpis
# dlatego podajemy wartosc domyslna wtedy gdyby nie bylo jeszcze klucza to wyswietl wartosc
# dodatkowo jeszcze ta wartosc jak i klucz zostanie dodane do dictionery 
# co pozwoli pozniej uzywac tego wpisu ze slownika
# print(CountryLeaders.setdefault('FR', 'Macron'))

# get(key) czyli chcemy wyswietlic wartosc dla klucza, jednak gdy ten klucz nie wystepuje w dictionery wowczas 
# wyswietli sie komunikat "none" a klucz nie zostanie dodany do slownika
# print(CountryLeaders.get('IT'))

# nowy slownik
NewLeaders = {'IT':'Berlusconi', 'DE':'Schulz'}

# metoda update dla starego slownika
# jesli wartosc z nowego slownika nie zostanie znaleziona w starym slowniku to ta wartosc zostanie dodana
# natomiast jesli klucz juz znajduje sie w slowniku to jego wartosc zostanie zmieniona na wartosc z nowego slownika
CountryLeaders.update(NewLeaders)


print(NewLeaders)
print(CountryLeaders)

# tworzenie nowego dictionery
chanels = {"Google" : 1480, "Email" : 300, "Natural Traffic" : 400, "TV Sport" : 700}

# wyswietlenie wartosci dla klucza
print(chanels["Email"])

# aktualizacja zlownika za pomoca nowego slownika
chanelsUpdate = {"Natural Traffic" : 520, "News" : 600}
chanels.update(chanelsUpdate)

# wyswietlenie wszystkich kluczy
print(chanels.keys())

# wyswietlenie wszystkich wartosci
print(chanels.values())

# usuniecie wartosci ze slownika po kluczu
chanels.pop("Email")


print(chanels)

























