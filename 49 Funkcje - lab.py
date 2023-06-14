# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:27:35 2023

@author: mateu
"""



import math


def GiveGeomSeqElement (a1 = 2, factor = 2, index = 2):
    
    # Budujemy moduł służący do obliczeń na ciągach geometrycznych
    '''
    funkcję GiveGeomSeqElement, która: -przyjmuje 3 parametry 
    a1 - o domyślnej wartości  2, która oznacza pierwszy element ciągu, 
    factor - o domyślnej wartości 2, która oznacza współczynnik ciągu geometrycznego, 
    index - o domyślnej wartości 2, która oznacza  który element ciągu ma być wyliczony
    '''
    
    # pow(x, y) podniesienie x do potegi y
    value = a1 * pow(factor,index-1)
    return value

print("Element 64:" , GiveGeomSeqElement(1,2,64))
print("----------------------------------------")


a1 = 3
factor = 2
maxindex = 10

for i in range(1,maxindex):
    
    an = GiveGeomSeqElement(a1 = a1, factor = factor, index = i)
    print("Term", i , "=", an)
    
print("--------------------------------------")    



def GiveFactoryFOrGeomSeq (term, nexterm):
    # Przygotuj funkcje GiveFactorForGeomSeq, która wyznaczy wartość współczynnika gdy znane są 2 kolejne wyrazy ciągu.

    return nexterm / term

print("Test function ", GiveFactoryFOrGeomSeq(12, 24))



def GiveSumOfNElementsGeomSeq (a1 = 2, factor = 2, n = 2):
    # Utwórz funkcję GiveSumOfNElementsGeomSeq, która wyznaczy sumę pierwszych wyrazów ciągu.
    
    sumN = a1 * (1 - pow(factor,n)) / (1 - factor)
    return sumN
    

print("Sum of n element is", GiveSumOfNElementsGeomSeq(2,3,4))





import geom
print('2^64 =',geom.GiveGeomSeqElement(1,2,64))

print('------------------------------------------------')
a1=3
factor=2
maxindex=11
for i in range(1,maxindex+1):
    an = geom.GiveGeomSeqElement(a1=a1,factor=factor,index=i)
    print('Term ',i,'=',an)
    
print('------------------------------------------------')
print('Factor is', geom.GiveFactorForGeomSeq(12,24))

print('------------------------------------------------')
print('Sum of n elements is', geom.GiveSumOfNElementsGeomSeq(2,3,4))





























