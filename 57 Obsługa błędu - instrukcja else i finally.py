# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:19:00 2023

@author: mateu
"""



import sys

taskPerPerson = 0

try:
    tasks = 32
    personsStr = input("How many persons are there is the team? ")
    persons = int(personsStr)
    
    taskPerPerson = tasks / persons
    
# except mozna zwrocic nazwe bledu, wowczas gdy dany blad wystapi mozna wyswietlic komunikat zwiazany z 
# obsluzonym bledem
# as e mozna przekazac do komunikatu dodatkowe informacje o bledzie
except ValueError as e:
    print("Sorry - you need to enter an integer number: ", e)    
    
except ZeroDivisionError as e:
    print("Sorry - you need to enter value > 0: ", e)    
    
    
except:    
    print("Smoething went wrong...", sys.exc_info()[0])

# jesli do zadnego bledu w bloku try nie doszlo to mozna uzyc polecenia else
else:
    print("Every person should have around ", taskPerPerson, "tasks")  

# bez wzgledu na to czy doszlo do bledu czy tez nie to w sekcji finally kod sie wykona zawsze
# jest to dobre miejsce do posprzatania wszystkiego co moglo sie zadziac w bloku try niezaleznie czy
# blad byl czy tez nie
finally:
    print("Script finished with/without errors")
    







import sys
import os

line = input("Podaj cene za kurs ktora by cie zadowala: ")
filepath = input("Wprowadz sciezke do pliku: ")

file = open(filepath, 'w')
file.write(line)
file.close()




line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    file.close()
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')



line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    value = int(line)
    file.close()
    print("The value saved is file is ", value)
except FileNotFoundError as e:
    print('Error opening file',filepath,e)
    
except ValueError as e:
    print("The value entered cannot be converted to a number ", e)
    
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')

else:
    print("Actions completed successfull")















