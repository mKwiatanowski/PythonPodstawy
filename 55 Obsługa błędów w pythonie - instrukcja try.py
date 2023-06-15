# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:18:59 2023

@author: mateu
"""

import sys

taskPerPerson = 0

# try dodajac to do jakiegos bloku, gdzie mozna by sie spodziewac jakiegos bledu, np przy wprowadzniu danych przez
# uzytkownika i jesli w tym bloku wystapi blad to wowczas zostanie wywolane except i program przejdzie dalej
# natomiast jesli wszystko przegiegnie ok to kod sie wykona a sekcja except zostanie pominieta
try:
    tasks = 32
    personsStr = input("How many persons are there is the team? ")
    persons = int(personsStr)
    
    taskPerPerson = tasks / persons
    
except:
    # sys.exc_info()[0] funkcja zwraca 3 kolumny z czego pierwsza zwraca tekst bledu do jakiego doszlo w skrypcie 
    
    print("Smoething went wrong...", sys.exc_info()[0])

print("Every person should have around ", taskPerPerson, "tasks")    










import sys



file_path = r'c:\temp\data_input\orders.csv'
 
with open(file_path,"r") as file:
 
    for line in file:
        
        try:
            line = line.replace('\n','')
            order = line.split(',')
     
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            
            print("Order from drugstore %s, item %s, amount %d " % (pharmacy_name, item, amount))
        
        except:
            print("Problem with line: ", line)
            print("Something when wrong....", sys.exc_info()[0])
 
 
print("Processing finished")




























