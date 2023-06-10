# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:25:47 2023

@author: mateu
"""


itRains = False

if itRains :
    print("We stay at home")
else :
    print("We go out")


# ternary operator skrócona wersja if 
# za pomoca print( Komunikat gdy warunek zostanie spelniony if warunek else i warunek gdy nie zostanie spelniony )
# takie zastosowanie jest dobra gdy chcemy zrobic prosty warunek umozliwajac skrocenie kodu do jednej linijki
print("we stay at home" if itRains else "We go out")



musclePain  = True
fever       = True
weakness    = True

if musclePain and fever and weakness:
    print("Suspicion of influenze")
else:
    print("The flu is unlikely")

print("----")


if musclePain and fever and weakness:
    print("suspicion of influenza")
elif not (musclePain and fever) and weakness:
    print("Just take a rest!")
else:
    print("you may be cold")

isMan = True

if musclePain and fever and weakness or  isMan and (musclePain or fever or weakness):
    print("suspicion of influenza")
elif not (musclePain and fever) and weakness:
    print("Just take a rest!")
else:
    print("this only cold")
 
    
 
checkList = True

print("Check is completed" if checkList else "Check not done yet")
 
    
 
    
 
    
 
    












