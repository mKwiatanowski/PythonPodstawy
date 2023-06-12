# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 16:37:35 2023

@author: mateu
"""



# instrukcja breake moze byc uzywana wewnatrz petli while lub petli for i jej zadaniem jest przerwanie wykonania petli
# zastosowanie w skutek zaistnialych warunkow stwiera sie ze dalsze wykonywanie petli nie ma sensu



# 1 sposob wyswietlenia liczby pierwszej ten sposob zadziała w bardzo zblizony sposob w innych jezykach programowania

for candidate in range(2,31):

    isPrime = True
    
    for divider in range(2,candidate):
        
        # jesli uda sie podzielic liczbe bez reszty to znaczy ze ta liczba nie jest liczba pierwsza
        if candidate % divider == 0:
            isPrime = False
            print("%2d is not a prime number - divider is %2d " % (candidate,divider))
            break
        
    if isPrime:
        print("%2d is prime" % (candidate))


# w pythonie jest mozliwosc innej skladni
# nie trzeba korzystac z dodatkowej zmiennej isPrime
# jest to polecenie else ale nie dla if tylko dla petli for
# w takim układzie else nie będzie się uruchamiać jesli w wewnetrzej petli uruchomi sie polecenie break4
# w przypadku zerwania petli funkcja break instrukcja else nie wykona sie

for candidate in range(2,31):

    for divider in range(2,candidate):
        
        # jesli uda sie podzielic liczbe bez reszty to znaczy ze ta liczba nie jest liczba pierwsza
        if candidate % divider == 0:
            isPrime = False
            print("%2d is not a prime number - divider is %2d " % (candidate,divider))
            break
        
    else:
        print("%2d is prime" % (candidate))




# jesli zastosuje potrujny cudzyslow na poczatku i koncu """ adfadsad """ to w samym kodzie bedzie mozna przeniesc test
# do nowej linii

text = """Mechanical advantage is a measure of the force amplification achieved by using a tool, 
mechanical device or machine system. The device preserves the input power and simply trades off forces 
against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. 
Machine components designed to manage forces and movement in this way are called mechanisms.[1] 
An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal 
mechanism does not include a power source, is frictionless, and is constructed from rigid bodies 
that do not deflect or wear. The performance of a real system relative to this ideal."""


# w petlii szukam w tekscie spacji, nastepnie do zmiennej counter dodaje 1 i wykonuje to do momentu az 
# zmienna bedzie rowna lub wieksza 20 wowczas wieswietla tekst ktory zapisalem do zmiennej short text i go wyswietlam
short_text = ''
# podział tekstu ze wzgledu na spacje
words = text.split(" ")
counter = 0

for word in words:
    short_text += word + " "
    counter += 1
    
    if counter >= 20:
        print(short_text)
        break
    



definitions = [
    'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.',
    'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
    'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar una carga de resistencia.',
    'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force importante transmise au système de freinage pour une course de faible distance.'  
    ]


# robiet to samo co wyzej tylko ze w pierwszej petli sprawdzam na liscie pierwsza pozycje z listy
# nastpenie w drugiej petli licze 20 slow i je wyswietlam


for definition in definitions:
    
    short_text = ''
    words = definition.split(" ")
    counter = 0
    
    
    for word in words:
        short_text += word + " "
        counter += 1
        
        if counter >= 20:
            print(short_text)
            break


















