# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:18:12 2023

@author: mateu
"""



import random

# lista z liczbami
myNumbers = []

while len(myNumbers) < 7:
    
    newNumbers = random.randint(1, 49)
    
    # jako że losowana liczba powinna wystapic tylko 1 raz to sprawdzam czy nowa liczba znajduje sie w juz istniejacej
    # liscie, a nastepnie za pomoca polecenia continue przeskakuje na poczatek petli nie dodajac tej liczby do listy
    if newNumbers in myNumbers:
        print("Eliminated: ", newNumbers)
        continue
    
    myNumbers.append(newNumbers)
    
print("My numbers is: ", myNumbers)    




# przykład karty

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']
allCards = []

for c in colors:
    for f in figures:
        allCards.append("%s - %s" % (c, f))

print(allCards)


# tasowanie kart

# random.shuffle() losowe wymieszanie zawartosci listy
random.shuffle(allCards)
print(allCards)


player1 = []
player2 = []

max = len(allCards)

for i in range(max):
    if i % 2 == 0:
        print(player1.append(allCards[i]))
    else:
        print(player2.append(allCards[i]))
    
print("-------PLAYER 1--------\n %s \n -------PLAYER 2--------\n %s " % (player1,player2))


# drugi sposob jesli wiemy ze jest 24 karty i rozdajemy karty rowno po 12 to mozna pierwszemu graczowi dac pierwsze 12 kart
# a drugiemu graczowie ostatnie 12 kart


print('-------PLAYER 1--------')
print(player1)
 
print('-------PLAYER 2--------')
print(player2)  


















