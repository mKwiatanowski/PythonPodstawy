# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 17:18:55 2023

@author: mateu
"""



# continue nalezy kojarzyc z petlami, jesli zostanie wykonane w petli to wtedy nie beda wykonywane kolejne instrukcje 
# w petli tylko sterowanie przeskoczy do warunku okreslajacego petle, czyli na poczatek petli


persons = ["Elizabeth","Steven@seles.mycompany.com","Sebastian","Margaret","Svetlana@mycompany.eu","Rapheal"]


domain = "mycompany.com"

emails = []


"""
# budowanie listy
for person in persons:
    
    # jesli na liscie wystepuje @ to zapisuje taki adres
    if "@" in person:
        emails.append(person)
        
    # jesli nie ma w nazie @ to tworze adres mail
    else:
        email = person + "@" + domain
        emails.append(email)

for email in emails:
    print(email)
"""


# to samo co wyżej tylko z wykorzystaniem countinue
# uzycie countinue sprawilo ze nie trzeba bylo wykonywac instrukcji else
# czyli jesli znalezlismy osobe z mailem to od razu przechodzimy do nastepnej osoby i nie interesuje nas
# warunek z tworzeniem nowego adresu mail 
# wiec jesli @ nie zostanie znaleziona to cale polecenie if sie nie wykona i od razu przechodzimy do kroku
# gdzie tworzymy nowy adres mail

for person in persons:
    
    if "@" in person:
        emails.append(person)
        continue
    
    email = person + "@" + domain
    emails.append(email)


for email in emails:
    print(email)






menu = '''
Choose what you want me to do for you:
1 - COFFEE
2 - TEA
3 - MAKE ME SMILE
---------------
To stop this script select 0
'''



smile = '''
 
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                                o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$
                                """"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$""""
'''



# pętla działająca w nieskończonosc
while True:
    
    print(menu)
    # input() służy do interaktywnego pobierania danych od użytkownika. Pozwala ona na wprowadzenie wartości 
    # z klawiatury i przypisanie ich do zmiennej.
    letter = input("Enter your choice  ")
    
    if letter == '1':
        print("Function COFFEE not implemented")
        input("Please press enter")
        continue
    
    if letter == '2':
        print("Function TEA not implemented")
        input("Please press enter")
        continue
        

    if letter == '3':
        print(smile)
        input("Please press enter")
        continue

    if letter == '0':
        break
    
    input("You need to make a valid choice. Press ENTER and try again!")


























