# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 18:35:32 2023

@author: mateu
"""



initialCapital = 20000
wynik = initialCapital
percent = 0.03
maxTimeYears = 10
i = 0

while i < maxTimeYears:
    i += 1
    wynik = round(wynik * (percent+1),2)
    
    print("Po roku ", i, "zarobiles ", wynik)
    
else:
    print("calkowity na inwestycji to ", wynik-initialCapital)




number = 20730906
tmp = number
suma = 0

while tmp > 0:
    tmpNumber = tmp % 10
    suma += tmpNumber
    tmp = tmp // 10
    
else:
    print("suma ", number, "to ", suma)







text = '''United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.'''

licz = 0
wordLenght = 6
tmpText = text.replace("\n", ' ').split(" ")
shortWord = 0
longWord = 0


while licz < len(tmpText):
    
    if len(tmpText[licz]) > wordLenght:
        longWord += 1
    
    elif len(tmpText[licz]) > 0:
        shortWord += 1

    licz += 1

print("Slowa krotse od ", wordLenght, ":", shortWord)
print("Slowa służsze od ", wordLenght, ":", longWord)
    
    
    








