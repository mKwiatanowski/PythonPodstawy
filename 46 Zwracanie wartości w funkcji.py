# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 09:59:16 2023

@author: mateu
"""



# zamiast wyswietlac w funkcji gotowy wynik, funkcja moze zwrocic obliczna wartoc.
# w tym celu po return nalezy umiescic zmienna ktora ma zostan zwrocna przez ta funkcje

from datetime import date
from datetime import timedelta    
    
def GiveWorkindDay(year     = date.today().year , \
                   month    = date.today().month , \
                   day      = date.today().day):   
    
    # prints the nearest working day date
    

    
    #day = date.today()
    day = date(year,month,day)
    
    
    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day
    

    return workingday


nextWorkingday = GiveWorkindDay(2017,9,2)
print("Next working day after", 2017,9,2, "is", nextWorkingday)
nextWorkingday = GiveWorkindDay()
print("Next working day after today is", nextWorkingday)

# dodatkowo jesli do funkcji nie beda wprowadzane zadne parametry to nie trzeba jej przypisywac do zmniennej
# rownie dobrze mozna ja wywolac bezposrednio

print("Next working day often today is", GiveWorkindDay())













def PrintAnimal(animal = ""):
    # this function prints a cat, bear or bat ascii-art
    

    txt_cat = r'''
    |\---/|
    | o_o |
     \_^_/'''
 

    txt_bear = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---` '''


    txt_bat = r'''
  /\                 /\
 / \'._   (\_/)   _.'/ \
/_.''._'--('.')--'_.''._\
| \_ / `;=/ " \=;` \ _/ |
 \/ `\__|`\___/`|__/`  \/
         \(/|\)/       '''
    

    if animal == "cat":
        
        print(txt_cat)
        
    elif animal == "bear":
        
        print(txt_bear)
        
    elif animal == "bat":
        
        print(txt_bat)
        
    else:
        
        print("Cannot print %s. Correct values for the parameter are: cat, bear, bat" % (animal))
        
        return False

    return True





if PrintAnimal():
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')
 
 
if PrintAnimal('dog'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')
 
 
if PrintAnimal('bat'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')











from datetime import date
from datetime import datetime


def DaysToEndOfYear(year    = date.today().year , 
                    month   = date.today().month ,
                    day     = date.today().day ):
    

    
    date_today = date(year,month,day)
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - date_today
   
    return delta.days



deltaDays = DaysToEndOfYear(2022,11,2)

print("Pozostala ilosc dni zwracana przez zmienna", deltaDays)

print("Pozostala ilosc dni zwracana przez funkcje", DaysToEndOfYear())

print("Pozostala ilosc dni zwracana przez funkcje", DaysToEndOfYear(month=4))








