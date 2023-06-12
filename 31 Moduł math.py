# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 17:32:45 2023

@author: mateu
"""

import math

f_smaller   = 3.141592653589793
f_bigger    = 3.87756392764

# math.ceil zwraca najmniejsza liczbe całkowitą ktora wieksza od przekazanego argumentu
# wiec dla liczby 3.5494 najmniejsza całkowita liczba wieksza od 3.5494 bedzie 4
print(math.ceil(f_smaller),math.ceil(f_bigger))
print("\n")

# math.floor zwraca najwieksza liczbe całkowitą ktora mniejsza od przekazanego argumentu
# wiec dla liczby 3.5494 najwieksza całkowita liczba mniejsza od 3.5494 bedzie 3
print(math.floor(f_smaller),math.floor(f_bigger))
print("\n")

# math.ceil najmniejsza liczba wieksza od -3.644 bedzie -3
print(math.ceil(-f_smaller),math.ceil(-f_bigger))
print("\n")

# math.ceil najwieksza liczba mniejsza od -3.644 bedzie -4
print(math.floor(-f_smaller),math.floor(-f_bigger))
print("\n")


# math.pow czyli podniesienie liczby do potęgi 2^8, również mozna policzyc pierwiastek z 9 bo 9 do 0.5 4
# to pierwiastek z 9
print(math.pow(2,8), math.pow(9,0.5))
print("\n")

# lepszym rozwiazaniem obliczniea pierwiastka jest math.sqrt pierwiastka kwadratowego
print(math.sqrt(16))
print("\n")


# stałe liczba pi i liczba e
print(math.pi, math.e)
print("\n")


print(math.sin(math.pi/2), math.cos(math.pi/4))





degree = 360

radian = degree * math.pi / 180
print("%d degree is %f radians" % (degree,radian))



degree = 45

radian = degree * math.pi / 180
print("%d degree is %f radians" % (degree,radian))



print("%d degree is %f radians" % (360,math.radians(degree)))
print("%d degree is %f radians" % (45,math.radians(degree)))


small_pizza_r   = 22
big_pizza_r     = 27
family_pizza_r  = 38

small_pizza_price   = 11.50
big_pizza_price     = 15.60
family_pizza_price  = 22.00


small_area = math.pi * small_pizza_r**2
big_area = math.pi * big_pizza_r**2
family_area = math.pi * family_pizza_r**2
 
print('small', small_pizza_r,small_pizza_price, small_area)
print('big', big_pizza_r,big_pizza_price, big_area)
print('family', family_pizza_r,family_pizza_price, family_area)      
print('')
print('small', small_pizza_price/small_area)
print('big', big_pizza_price/big_area)
print('family', family_pizza_price/family_area)
print('')
      

# wywolania funkcji jakie nzajduja sie w medule
math_ls = dir(math) 
print(math_ls)

















