# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 15:42:56 2023

@author: mateu
"""



# importowanie modulu
# import math

# print(math.pi)

# zawsze nalezy wskazac na modul z jakiego pochodzi dana funkcja
# print(pi)


# jesli zresetuje sie shella to wszystkie zaladowane do niego moduly znikna i odwolanie sie ponownie do 
# jakiejsc funkcji np math.pi zakonczy sie niepowodzeniem


# inny sposob na wywolanie funkcji, gdy w taki sposob wczyta sie modul to pozniej nie trzeba pisac odwolania do 
# niej aby wywolac funkcje

# from math import *

# print(pi)

# print(floor(pi))


# jesli sie importuje modul za pomoca polecenia " import modul " to tworzy sie nowy podkatalon w systemie plikow
# jesli uzyje sie drugiego sposobu " from math import * " wowczas te funkcje beda zaimportowane do katalogu glownego

# minusem tego rozwiazania jest to ze jesli zaimportujemy dwa rozne moduly gdzie beda sie znajdawac funkcje o tej 
# samej nazwie to te funkcje sie nawzajem przykryja wiec przy pierwszym sposobie odwolujac sie do modulu
# bez problemu bedzie mozna uzywac funkcji o tej samej nazwie





# przy pisaniu kodu lepszym sposobem jest uzywanie tego pierwszego sposobu



import statistics


percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,

           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,

           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,

           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,

           8.740978348,6.174819567]

percent.sort()


print(percent)

print(statistics.median(percent))
print(statistics.median_low(percent))
print(statistics.median_high(percent))



from statistics import *


print(median(percent))
print(median_low(percent))
print(median_high(percent))


















