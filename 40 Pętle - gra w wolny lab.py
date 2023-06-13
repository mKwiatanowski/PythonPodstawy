# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 11:58:17 2023

@author: mateu
"""



# gra w wojne
# jeżeli obaj gracze dadzą taką samą kartę to te karty wracają na koniec talii

# słownik
aCard = {"Figura":"King", "Power":12}
print(aCard)
print(aCard["Figura"])
print(aCard["Power"])

# dodanie koloru do słownika
aCard["Color"] = "Heart"
print(aCard["Color"])


# ----------------------------------------------


colors = ["Hearts", "Diamonds", "Clubs", "Spades"]

# Wewnątrz listy tworzenie slownika
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []

for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard["Color"] = c
        allCards.append(aCard)


import random

random.shuffle(allCards)

print(allCards,"\n\n")


player1 = []
player2 = []
'''
maxCard = len(allCards)

for m in range(maxCard):
    if m % 2 == 0:
        player1.append(allCards[m])
    else:
        player2.append(allCards[m])
'''        
player1 = allCards[:12]
player2 = allCards[12:]       
      

print("player1: \n %s \n\n player2 \n %s" % (player1,player2))


while len(player1) > 0 and len(player2) > 0:
    # pop pobiera element z listy usuwa go z tej listy a nastepnie zwraca ten element
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    
    # jesli sila obu kart jest taka sama to pobrane karty wracaja na koniec talii posiadanej przez gracza
    if card1["Power"] == card2["Power"]:
        player1.append(card1)
        player2.append(card2)
        print('=EQUAL \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    
    # jeżeli carta1 ma wieksza moc od kary2 to obie karty przepisz do gracza 1
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
        
    else:
        player2.append(card2)
        player2.append(card1)
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')

if len(player1) > 0:
    print("Player1 won")
else:
    print("Player2 won")































