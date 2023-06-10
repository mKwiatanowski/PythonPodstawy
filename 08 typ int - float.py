# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 13:16:38 2023

@author: mateu
"""

five = 5 
tree = 3
five * tree

type(five)

type(five * tree)

five / tree

type(five / tree)


import sys

sys.maxsize


verybigvalue = 99999999999999999999999999999999999999999999999

type(verybigvalue)


(verybigvalue + 1) / 2
type ((verybigvalue + 1) / 2)


# // dzielenie całkowite (ilosc 3 ktore mieszcza sie w 5)
five // tree

# asd reszta z dzielenia
five % tree


name = "Mateusz"
age = 32
daysinYear = 365
message = "%s is %d years odl, so is about %d days old"
print(message % (name,age,age*daysinYear))

name = "Agata"
age = 25
daysinYear = 365
message = "{0:s} is {1:d} years odl, so is about {2:d} days old"
print(message.format(name, age, age * daysinYear) )

print("1234567890 divided by 12345 is", 1234567890 // 12345, " and the rest is" , 1234567890 % 12345)








