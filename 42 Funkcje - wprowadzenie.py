# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:35:29 2023

@author: mateu
"""



"""
Funkcje w Pythonie są blokami kodu, które wykonują określone działania i mogą być wywoływane w różnych miejscach 
w programie. Funkcje służą do zorganizowania kodu na mniejsze, bardziej czytelne i modułowe części, które mogą
być wielokrotnie używane.
Funkcje w Pythonie mają nazwę, listę argumentów (opcjonalnie), ciało funkcji i zwracaną wartość (opcjonalnie)
"""



# dobrą praktyką jest dodawanie wewnątrz funkcji komentarza opisujacego co ta funkcja robi
def PrintHello():
    #this functions just prints hello
    print("Hello")
    return



# aby wowolac funkcje nalezy wpisac jej nazwe()
PrintHello()



def PrintCat():
    txt = r'''
    |\---/|
    | o_o |
     \_^_/'''
    print(txt)
    return
 
    
def PrintBear():
    txt = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---` '''
    print(txt)
    return


def PrintBat():
    txt = r'''
  /\                 /\
 / \'._   (\_/)   _.'/ \
/_.''._'--('.')--'_.''._\
| \_ / `;=/ " \=;` \ _/ |
 \/ `\__|`\___/`|__/`  \/
         \(/|\)/       '''
    
    print(txt)
    return







PrintCat()
PrintBear()
PrintBat()
























































