# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 13:46:23 2023

@author: mateu
"""

i       = 1
imax    = 10

while i <= imax:
    print(i, "I like python")
    i+=1
else:
    print("Now i =",i)



i       = 10
imax    = 0

while i >= imax:
    print(i, "I like python")
    i-=2
else:
    print("Now i =",i)




firstRow        = 1
lastRow         = 31
currentRow      = firstRow

while currentRow <= lastRow :
    print("Row number ", currentRow)
    currentRow += 1



z       = 1
zmax    = 13
start   = z

while start <= zmax:
    print("Kwadrat liczby ", start , "to: ", start**2)
    print("Szescian liczby ", start , "to: ", start**3)
    start += 1



x       = 1
xmax    = 10
numer   = x

while numer <= xmax:
    print(numer, " | ", numer * "x")
    numer += 1






















