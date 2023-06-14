# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 09:18:56 2023

@author: mateu
"""



# jesli sa zdefiniowane parametry y, m, d to podczas wywoływania jesli, nie wprowadzi sie jego wartosci wyskoczy blad
# mozna tez zalozyc ze jakis parametr nie jest wymagany do podania przez uzytkownika 
# Wtedy mozna ustalic domyslna wartosc dla tego parametru d = 1 i jesli uzytkownik nie wporwadzi innej wartosci
# to taka wartosc domyslna zostanie pobrana do funkcji


# def GiveWorkindDay(year,month=1,day=1):
    
    
# można też w takim przypadku założyć, że jesli nie zostana podane zadne parametry to zostanie pobrana biezaca
# data, ale w tym celu trzeba pamietac aby przed tworzeniem funkcji byly zadeklarowane niezbedne moduly
    
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
    
    
    print("Working day for", day, "is", workingday)

    return


GiveWorkindDay(2017,9)
GiveWorkindDay(2017,9,3)
GiveWorkindDay(2017)


# w takim wypadku jesli nie podbamy zadnego parametru to zostanie pobrana data dzisieja
# jesli wprowadzimy np rok, to miesiac i dzien zostanie pobrany z dzisiejszej daty
# trzeba madrze uzywac wartosci domyslnych parametru bo na tym przykladzie moze byc dzis dzien 31 danego miesiaca
# a zostanie wprowadzona data 2017-02 a jak wiadomo w lutym nie ma 31 dni
GiveWorkindDay()
GiveWorkindDay(2017,2)












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

    return

PrintAnimal()





from datetime import date
from datetime import datetime


def DaysToEndOfYear(year    = date.today().year , 
                    month   = date.today().month ,
                    day     = date.today().day ):
    

    
    date_today = date(year,month,day)
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)



DaysToEndOfYear(2020,12,20)
DaysToEndOfYear(2021,12,21)
DaysToEndOfYear(year = 2022, month = 12, day = 22)
DaysToEndOfYear(day = 23, month =12, year = 2023)


DaysToEndOfYear()
DaysToEndOfYear(2017)
DaysToEndOfYear(month=2)
DaysToEndOfYear(day=1)










































