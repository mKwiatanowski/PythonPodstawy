# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 13:51:53 2023

@author: mateu
"""
"""
Chociaż Python ma już długą historię i chociaż powstaje w nim mnóstwo oprogramowania, to ma też kilka chorób "wieku dziecięcego"... i aż dziwi, że jeszcze z nich nie wyrósł.

Podczas wypuszczania nowszych wersji Pythona, nie zawsze jest zachowywana kompatybilność wsteczna. Tak było przy przejściu między wersją 2.x i 3.x.  Niestety skutkiem tego jest to, że całe oprogramowanie stworzone w wersji 2.x musiało zostać przepisane na wersję 3.x! To bardzo źle, bo to przecież mnóstwo pracy...

Teraz masz okazję doświadczyć tego na własnej skórze. Od wersji 3.7 pojawiają  się pewne zmiany w pracy z funkcja clock() z modułu time. Otóż ta funkcja nie jest już dostępna. Zamiast clock() należy korzystać z innych funkcji. Wspominam o tym, bo w kolejnym materiale video znajdziesz jeszcze informację o funkcji clock()

Zobacz jak obejść ten problem:
"""
import time
 
# sprawdzenie wersji pythona
import sys
print(sys.version)
 
# zamiast
# print(time.clock(), time.localtime(time.clock()))
# korzystaj z funkcji time.perf.counter():
print(time.perf_counter(), time.localtime(time.perf_counter()))



# funkcja time() zwraca czas ale ten czas jest zwracany w sposob  poczatek swiata unic 1970,01,01 i kręci sie 
# z predkoscia 1 na sekunde czyli liczba przed przecinkiem to ilosc sekund jaka minela do tej pory od poczatku
# swiata unixowego
print("Current time is... unix epoch", time.time())
print("\n")

# time.localtime(time.time()) zwraca obecny czas w formie tuple
print("Current time is... tuple", time.localtime(time.time()))
print("\n")

# time.asctime(time.localtime(time.time())) dopiero tak skonstruowana funkcja pozwala przedstawic czas
# w formie zrozumialej dla czlowieka dzien miesiac dzien i godzina rok 
# zostalo to wygenerowane bez mozliwosci modyfikowania sposobu wyswietlenia tej daty
print("Current time is... for human", time.asctime(time.localtime(time.time())))
print("\n")

print("\n\n\n\n")



import calendar


print("---------------------------------------")

# calender.month(rok, miesiac, w = 5) wyswietlenie kalendarza za okreslony miesiac
# w = 5 czyli na kazdy dzien jest przeznaczone 5 znakow
# l = 2 czyli odstepy miedzy liniami maja wynosic 2
print(calendar.month(2023, 6, w=5, l = 2))


# funkcja bez dodatkoowych parametrow to wysokosc i szerokosc bedzie miala minimalne wartosci 
# i bedzie bardziej kompaktowy
print(calendar.month(2023, 6))

# calendar.weekday(data) okreslenie dnia tygodnia w okreslonej dacie w zakresie od 0 do 6 gdzie 6 to niedziela
print("week day is ", calendar.weekday(2023, 6, 11))

# ustalenie od jakiego dnia tygodnia ma rozpoczynac sie tydzien 6 - niedziela
# wiec ma to wplyw tylko na to od jakiego dnia tygodnia zaczyna sie rysowac kalendarz 
# trzeba pamietac ze ta funkcja wplywa tylko i wylacznie na to jak kalendarz jest rysowany nie wplywa na inne funkcje
calendar.setfirstweekday(6)
print(calendar.month(2023, 6))

# calendar.isleap(rok) sprawdzenie czy rok przekazany jako parametr jest przestepny czy tez nie T / F
print("Is 2020 a leap year ", calendar.isleap(2020))

# calender.leapdays(x,,y) sprawdza zakres od x do y -1 czyli jesli za y damy 2020 to sprawdzany bedzie 2019
print("Leap days 2000-2017", calendar.leapdays(2000, 2017))
print("Leap days 2000-2020", calendar.leapdays(2000, 2020))
print("Leap days 2000-2021", calendar.leapdays(2000, 2021))







print(time.time())
print(time.localtime(time.time()))


print(calendar.month(2023, 10))

calendar.setfirstweekday(6)
print(calendar.month(2023, 10))

print("Czy 2020 byl rokiem przestepnym ", calendar.isleap(2000))


print(calendar.calendar(2019))













