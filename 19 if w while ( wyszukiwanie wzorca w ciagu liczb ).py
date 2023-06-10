# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:11:43 2023

@author: mateu
"""

# znalezienie 3 liczb ktore sa rosnace
values = [10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]

# zaczynamy od zera poniewaz 0 jest pierwsza pozycja w tym ciagu
i = 0

# len sprawdzenie przez literacje wielkosci ( wyliczy dlugosc tabeli )
max = len(values)-2

# zbadanie czy i jest mniejsze od max 
while i < max:
    print(i, values[i], values[i+1],values[i+2])
    
    # sprawdzenie czy 3 kolejne liczby są od siebie większe
    if values[i] < values[i+1] and values[i+1] < values[i+2]:
        print('\tFound: ', values[i], values[i+1],values[i+2])

    i += 1




numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i = 0
max = len(numbers)-1

# znalezienie liczby ktorek pierwsza do kwadratu rowna sie drugiej
while i < max:
    print(i, numbers[i], numbers[i+1])
    
    if numbers[i]**2 == numbers[i+1]:
        print("\tFOUND!")
        
    i += 1



# znalezienie liczby ktora pierwsza do kwadratu rowna sie drugie i druga do kwadratu rowna sie trzecie


numbers2 = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i2 = 0
max2 = len(numbers2)-2
while i2 < max2:
    print(i2, numbers2[i2],numbers2[i2+1],numbers2[i2+2])
    
    if numbers2[i2]**2 == numbers2[i2+1] and numbers2[i2+1]**2 == numbers2[i2+2]:
        print("\tFound")
    
    i2 += 1
        


# znalezienie przypadku gdzie dlugosc pierwszego argumentu jest rowna dlugosci drugiego argumentu

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


z = 0
tabMax = len(texts)-1

while z < tabMax:
    print(z, texts[z], texts[z+1])
    
    # sprawdzenie długosci pierwszego argument i porownanie go z dlugoscia drugiego argumentu
    if len(texts[z]) == len(texts[z+1]):
        print("\tFound")
    
    z += 1
































