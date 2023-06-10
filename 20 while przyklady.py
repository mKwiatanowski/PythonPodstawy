# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 09:35:42 2023

@author: mateu
"""

# paczki o wadze w kg
cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort()
cargo.reverse()

print("The cargo list is: ", cargo)

# max waga paczki
boxCapacity = 90

# podło do wloze paczek  
box = []
i = 0

# dopuki suma elementow na tej liscie i nastepny element dodany z listy jest mniejszy jak max waga paczki
# to dodaj kolejny elememnt z listy
# gdbyby suma elementow z listy byla mniejsza jak max pojemnosc paczki to petla nigdy by sie nie skoczyla
# wiec trzeba jeszcze dodac warunek w ktorym sprawdzimy czy numer aktualnie sprawdzanego elemento jest wiekszy od 
# dlugosci listy

# while sum(box) + cargo[i] < boxCapacity and i < len(cargo):
#    box.append(cargo[i])
#    i += 1

# teraz przetwarzamy dane tak długo gdzie ilosc wolnego miejsca w pudle jest wieksza badz rowna 
# od najmniejszego elementu listy
while  i < len(cargo) and (boxCapacity - sum(box) >= min(cargo)) :
    
    # element mozna wlozyc tylko gdy spelniony jest warunek gdzie wielkosc pudelka pomniejszony o sume juz wlozonych 
    # elementow jest wieksza badz rowna od nastepnego badanego elementu wowczas taka wartosc mozna dodac do pudelka
    if (boxCapacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i += 1



print("The collected items sum is: ", sum(box))
print("The element are: ", box)




number = 1
previosNumber = 0

while number <= 50:
    print(previosNumber + number)
    previosNumber = number
    number += 1
    



import random
my_number = random.randint(0, 20)
guess = -1

print("Guess my number")

while guess != my_number:
    
    guess = int(input())
    
    if guess == my_number:
        print("You are right It was:", my_number)
    elif guess > my_number:
        print("Sorry my numer is smaller that your", guess, "ry again")
    else:
        print("Sorry my numer is grater that your", guess, "Try again")
            



import random
my_number = random.randint(0,20)
guess=-1
trials = 0
 
print("Guess my number!")
 
while guess != my_number :
 
    guess = int(input())
    trials+=1
    
    if guess == my_number:
        print("You are right! It was:",my_number,"You needed",trials,"trials.")
    elif guess>my_number:
        print("Sorry- my number is smaller than", guess, "Try again!")
    else:
        print("Sorry- my number is greater than", guess, "Try again!")




































