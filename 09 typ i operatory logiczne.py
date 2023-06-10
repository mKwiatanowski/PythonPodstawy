# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 13:38:12 2023

@author: mateu
"""


isWeekend = False
print("Is weekend = ", isWeekend)

Temperature = 5
print("Temperature = ", Temperature)

ToDoList = 'Zakypy'
print ("ToDoList = ", ToDoList)

# == sprawdzenie czy wartosc rowna jest innej wartosc
IsHappy = isWeekend and Temperature >= 20 and ToDoList == ''
print("IsHappy = ", IsHappy)

# != sprawdzenie czy wartosc jest rozna od sprawdzanej wartosc
IsHappy = not isWeekend and Temperature < 20 and ToDoList != ''
print("IsHappy = ", IsHappy)


# jesli linijka kodu jest za dluga to na koncu nalezy dac znak \ a nastepnie mozna po enterze pisac w nowej lini
IsHappy = not isWeekend and Temperature < 20 and ToDoList != '' \
    or isWeekend and Temperature >= 20 and ToDoList == ''
print("IsHappy = ", IsHappy)


# przykładowo jesli mamy warunek Temperature >= 20 ale chcemy sprawdzic w druga strone to nie musimy zmieniac
# znaku z >= na <= wystarczy ze przed warunkiem dodamy not Temperature >= 20


# is the light switch in AUTOMATIC mode
isAutomaticMode     = True 

# is the level of day-lighr above 80%
is80PercentLight    = True

# is the Sun ligthing directly into the driver's face
isDirectLight       = False

# is it rainy, foggy or other weather conditions are present
isRaing             = False

turnLightOn         = isAutomaticMode and ( is80PercentLight or not isDirectLight or  isDirectLight)




print("Automatic mode:      ", isAutomaticMode)
print("Is the light good:   ", is80PercentLight)
print("Is sun low:          ", isDirectLight)
print("Is it rainy:         ", isRaing)
print("Trun Light on:       ", turnLightOn)





































