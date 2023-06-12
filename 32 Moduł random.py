# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 18:02:20 2023

@author: mateu
"""



# generowanie licz losowych

import random

# random.randint wylosuje liczbe calkowita w pełnym zakresie z () 1 <= n <= 100
print("One random number: ", random.randint(1, 100)) 
print("\n")

# random.choice wybierze jednąa pozycje z zadanej listy
print("Choosing rundom number from a range ", random.choice(range(1, 100)) )
print("\n")

# random.randrange skrocona forma random.choice(range(1, 100))
print("Choosing rundom number from a range ", random.randrange(1,100))
print("\n")


list = ["John","Ann","Peter","Susan","Emily","Greg","Chris",]

# random.shuffle przekazuje liste i wynikiem tego bedzie losowe wymieszanie zawartosci listy
random.shuffle(list)
print("Reordered list:", list)
print("\n")



# random.random() losuje dowolna liczbe z zakresu od 0 do 1 ( po przecinku )
print("Just a random float", random.random()) 
print("\n")






z = 1
zbior = 10

while z <= zbior:
    print("Losowanie nr %d, z zakresu od 1 do 100. Wynik to: %d" % (z, random.randint(1, 100)))
    z += 1

# inny sposob z wykorzystanie for

# range(10) oznacza generowanie sekwencji liczb całkowitych zaczynającej się od 0 (domyślnie) 
# i kończącej się na 9 (10 nie jest włączone).
for i in range(10):
    print(random.randint(0, 100))



number1 = random.randint(1, 100)
counter = 0
number2 = random.randint(1, 100)


while number1 != number2:
    counter += 1
    number2 = random.randint(0, 100)
    print("próba nr %d: Wylosowana liczba number2 to: %d" % (counter,number2))

print("Potrzebne było %d prób aby liczba1 %d została wylosowana ponownie w zbiorze liczba2 %d " % (counter,number1,number2))







countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]



random.shuffle(countries)

groupNumber = 0

for i in range(len(countries)):

    if i % 4 == 0:
        groupNumber += 1
        print("---- Grupa %d ----" % (groupNumber))

    print(countries[i])




