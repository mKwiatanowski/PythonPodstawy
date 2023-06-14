# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 15:58:50 2023

@author: mateu
"""


# w nawiasie wpisujemy jakie parametry maja byc przekazane do funkcji
def GiveWorkindDay(year, month, day):
    
    # prints the nearest working day date
    
    from datetime import date
    from datetime import timedelta
    
    #day = date.today()
    day = date(year, month, day)
    
    
    if day.weekday() == 5:
        workingday = day + timedelta(days=2)
    elif day.weekday() == 6:
        workingday = day + timedelta(days=1)
    else:
        workingday = day
    
    
    print("Working day for", day, "is", workingday)

    return






GiveWorkindDay(2017, 9, 30)
GiveWorkindDay(2017, 10, 1)
GiveWorkindDay(2017, 10, 2)
GiveWorkindDay(2017, 10, 3)
GiveWorkindDay(2017, 10, 4)
GiveWorkindDay(2017, 10, 5)
GiveWorkindDay(2017, 10, 6)
GiveWorkindDay(2017, 10, 7)


GiveWorkindDay(year=2017, month=12, day=6)
GiveWorkindDay(day=6, month=12, year=2018)

#GiveWorkindDay(year, month, day)








def PrintAnimal(animal):
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

PrintAnimal("bdsf")





def DaysToEndOfYear(year, month, day):
    
    from datetime import date

    
    date_today = date(year,month,day)
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)



DaysToEndOfYear(2020,12,20)
DaysToEndOfYear(2021,12,21)
DaysToEndOfYear(year = 2022, month = 12, day = 22)
DaysToEndOfYear(day = 23, month =12, year = 2023)












