# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 10:48:04 2023

@author: mateu
"""



persons = ["Elizabeth","Steven","Sebastian","Margaret","Svetlana","Rapheal"]

domain = "mycompany.com"


# przy petli for na poczatku wymyslam jakas nazwe w tym wypadku przetwarzam liste osob persons to pojedyncza osobe
# nazwe sobie person nastepnie in a pozniej lista i :
    # gdy program doszedl do petli for utowrzyl zmienna person i pobral do niej pierwsza wartosc z listy persons
for person in persons:
    # nastepnie dla pierwszej pozycji zostal stworzony adres mail i wyswietlony 
    email = person + "@" + domain
    print("Email for \t", person, "\tis\t", email)

else:
    print("end of the list")






data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']


for s in data:
    print(s.upper())


for error in data:
    error = error.split(":")
    print(error[0].upper(), "\t ", error[1])



for elem in data:
    elem = elem.split(":")
    
    if elem[0] == "Error":
        print(elem[1].upper())
    else:
        print(elem[1])
    
    
    
 





























