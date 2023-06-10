# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:11:18 2023

@author: mateu
"""

# gorszy sposob pisania zlozonej petli if

age = 12
isDrunk = False    
isResticiedArea = False


if age < 18 :
    print("Jestes za mlody")
else :
    if isDrunk :
        print("Jestes piany? Nie sprzedam ci alkoholi")
    else :
        if isResticiedArea :
            print("Jestes w strefie ograniczenia sprzedazy alkoholu")
        else:
            print("Ok mozesz kupic alkohol")

print("-----")

# lepszy sposób pisania warunku if i elif

if age < 18 :
    print("Jestes za mlody")
elif isDrunk :
    print("Jestes piany? Nie sprzedam ci alkoholi")
elif isResticiedArea :
    print("Jestes w strefie ograniczenia sprzedazy alkoholu")
else :
    print("Ok mozesz kupic alkohol")



















