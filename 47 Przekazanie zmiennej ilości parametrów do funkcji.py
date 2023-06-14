# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 11:09:25 2023

@author: mateu
"""



def DoAction (action, parameter):
    print("action:", action)
    print("parameter:", parameter)
    return


DoAction("buy", "aahoes")



# jesli parametr bedzie poprzedzony * ta * oznacza ze to co przychodzi do funkcji nie jest pojedynczym elementem
# ale kolecja elementow " tople "
def DoAction2 (action, *parameter):
    print("action:", action)
    print("parameter:", parameter)
    
    # dodajemy element iteracji
    for element in parameter:
        print("element is", element)
    
    return


DoAction2("buy", "aahoes", "socks", "t-shirt")



'''
Podwójny znak gwiazdki (**) przed parametrem "parameter" w definicji funkcji oznacza, 
że parametr ten jest traktowany jako słownik (dictionary) z nazwami argumentów i ich wartościami.
Jest to po prostu obiekt dictionery
'''

def DoAction3 (action, what, **parameter):
    print("action:", action)
    print("what:", what)
    print("parameter:", parameter)
    
    # kiedy pracujemy ze slownikiem podejscie jest troche inne do iteracji
    for element in parameter:
        
        # tutaj parametr element jest kluczem w slowniku, a zeby wyciagnac wartosc dla tego klucza
        # nalezy na liscie wywolac dla wskazanego klucza jego wartosc
        print(element, "=", parameter[element])
    
    return


DoAction3("buy", "shoes", size = 45, color = "brown", typ = "sport")











def PrintAnimal (*animal):
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
    

    for a in animal:
        if a == "cat":
            
            print(txt_cat)
            
        elif a == "bear":
            
            print(txt_bear)
            
        elif a == "bat":
            
            print(txt_bat)
            
        else:
            
            print("Cannot print %s. Correct values for the parameter are: cat, bear, bat" % (a))
            

    return 



PrintAnimal("cat", "bat", "dog")
PrintAnimal()










from datetime import date
from datetime import datetime


def DaysToEndOfYear (*dates):
    

    for data in dates:
        

        date_end_year = date(data.year , 12, 31)
        delta = date_end_year - data
        print("Dzisiejsza data to", data , "a pozostala ilosc dni do sylwestra to:" , delta.days)
       
    return 





DaysToEndOfYear(date(1999,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15),date(2019,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15),date(2019,1,15),date.today())















