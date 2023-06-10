# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 10:44:50 2023

@author: mateu
"""

age = 25


# budowa warunku
# if nastepnie warunek logiczny nasteonie :  jezeli pewna instrukcja ma sie wykona pod spelnieniu warunku
# to nastpnie w nowej lini fragment kodu musi byc wciety tabulator
if age >= 18 :
    print("You are aduit and you can buy alcohole")
else :
    print("You are too young to buy alcohole")    



isDrunk = False

if age >= 18 and not isDrunk:
    print("You are aduit and you can buy alcohole")
else :
    print("Sorry, we cannot sell you alcohole")    


isResticiedArea = False

if age >= 18 and not isDrunk and not isResticiedArea :
    print("You are aduit and you can buy alcohole")
else :
    print("Sorry, we cannot sell you alcohole")   



minLikes = 500
minShares = 100

numLikes = 1300
numShares = 654


if minLikes <= numLikes and minShares <= numShares :
    print("Super cena leci w dół o 10%")
else :
    print("Niestety wciąż czegos brakuje")    



isPizzaOrdered      = False
isBigDringOrdered   = False
isWeekend           = True

if (isPizzaOrdered or isBigDringOrdered) and not isWeekend :
    print("Super dostaniesz kod rabatowy na burgera")
else :
    print("ups tym razem nic z tego")


diskSize = 140
diskSizeUsed = 133
fileSize = 3

if (diskSize - diskSizeUsed) >= fileSize:
    print("File can be downloaded")
else :
    print("Sorry cannot be dowloaded file size to hight ")























