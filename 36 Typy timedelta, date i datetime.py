# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:31:15 2023

@author: mateu
"""


# datatime jest swiadom roku przestepnego, ale nie jest swiadom sekund przestepnych
import datetime

# poczatek swiata rok 1 koniec swiata rok 9999
print("Min and max", datetime.MINYEAR,datetime.MAXYEAR)

# typ datetime zajmuje sie czasem i data
# wektor czasu o jaki musimy sie przesunac do przodu lub do tylu
d1 = datetime.timedelta(days=1,hours=2,minutes=-30 )
print(d1)

d2 = datetime.timedelta(days=-1,hours=-2,minutes=-3)
print(d2)

print("timedelta:", d1+d2)
print("\n\n\n")


# typ date zajmuje sie tylko data
# wywolanie dzisiejszej daty
print("Today is:", datetime.date.today())
print("\n")

# przypisanie dzisiejszej daty do zmiennej
today = datetime.date.today()
# np termin zaplacenia faktury to 7 dni
daysToPay = datetime.timedelta(days=7)

print("Today is", today)
# zmienna.days czyli wyswietlenie tylko wartosci dni
print("Bills should be paid winthin:", daysToPay.days, "days")
print("The bill should be paid till:", today + daysToPay)
print("\n")



# koniec swiata wg pythona
endOfTheWorld = datetime.date.max
print("The final end od world will happen by python :", endOfTheWorld)
# jaki to bedzie dzien tygodnia
print(endOfTheWorld.weekday())
print("\n")


# obliczenie ile zyje dni ktos kto urodzil sie 2000-08-15
bornDate = datetime.date(2000,8,15)
today = datetime.date.today()
print(today - bornDate)
print("\n")


# datetime.datetime opis daty i godziny 
# pierwsze datetime to odwolanie do podfolderu w pythonie odpowiadajacemu zaimportowanemu modulowi
# drugie datatime to odwolanie do funkcji datatime ktora znajduje sie w module datatime
# mozna skrocic ten zapis, wowczas nalezy zastosowac zapis from datatime import datatime
# wowczas nie trzeba bedzie podawac na poczatku nazwy modulu

# now i today jest odniesieniem do czasu jaki znajduje sie na komputerze, tu moze zostac zmieniona strefa czasowa
# i bedzie pokazywac inny czas niz jest w rzeczywistosic w danej strefie czasowej
print("now() ", datetime.datetime.now())
print("today() ", datetime.datetime.today())
# utcnow czas greenwich w zakezbiscu od czasu letniego czy zimowego roznica bedzie wynosic od 1 do 2 godzin
print("utcnow", datetime.datetime.utcnow())
# weekday wskazanie numeru dnia tygodnia
print("weekday", datetime.datetime.today().weekday())

# strftime konwertowanie czasu do napisu
# %a oznacza skrocona nazwe dnia tygodnia
print("%a", datetime.datetime.now().strftime("%a"))
# $A oznacza pewlna nazwe dnia tygodnia
print("%A", datetime.datetime.now().strftime("%A"))
# $W oznacza numer dnia tygodnia tu uwaga niedziele liczymy jako 1 dzien tygodnia
print("%w", datetime.datetime.now().strftime("%w"))

print("%a %A %w", datetime.datetime.now().strftime("%a %A %w"))

# przykladowe zapisanie daty i czasu gdy np bedzie potrzeba do nazwy zapisanego pliku dodac godzine i czas jego zapisu

"""
%Y format liczbowy roku xxxx
%m format liczbowy miesiaca xx
%d format liczbowy dnia xx
%H format liczbowy godzinowy xx 0-24
%M format liczbowy minutowy xx
%S format liczbowy sekundowy xx
%f format liczbowy milisekundowy xxxxxx
"""


print("%Y-%m-%d_%H_%M_%S_%f" \
      , datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S_%f"))






















