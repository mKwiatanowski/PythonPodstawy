# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:59:53 2023

@author: mateu
"""



# filename = input("Enter filename: ")

# print("The file name is: %s " % (filename))

# specyfine dzialanie imput przy znaku \, po wywolaniu jest on dublowany 
# na ten moment uzytkownik moze wprowadzic cokolwiek, jednak sprawdzenie sciezki do pliku bedzie sprawdzenie pozniej
# filename


# funkcja input wszystko co czyta to tekst 
filesizeStr = input("Enter the max file size (MB): ")

# po dokonaniu konwersji tekstu na liczbe mozna juz dokonywac dzialan na liczbach
filesizeInt = int(filesizeStr)




print("The max size is %d" % (filesizeInt))

# w takim wypadku python zrozumie, że tekst ktory wprowadzamy chcemy powtorzyc 1024x 
# zeby dzialanie bylo zgodne matematycznie trzeba dokonac konwersji
print("Size in KB is %d" % (filesizeInt * 1024))



# zabezpieczenie sie na wypadek gdyby uzytkownik wpisal slownie liczbe
# wydawac by sie moglo ze petla ktora zwraca zawsze True bedzie dziala w nieskonczonosc
# jednakze jesli w warunkach uzyjemy polecenia break to znaczy ze ma przerwac petle
while True:
    
    filesizeStr = input("Enter the max file size (MB): ")
    
    # isdecimal() jest to funkcja ktora sprawdza czy wprowadzona wartosc przypomina liczbe
    if filesizeStr.isdecimal():
        filesizeInt = int(filesizeStr)
        break
    
print("The max size is %d" % (filesizeInt))
print("Size in KB is %d" % (filesizeInt * 1024))    






import math



def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

print('This program solves equation ax^2+bx+c = 0')
print('Enter the values for a, b and c:')


a_str = input("a = ")
b_str = input("a = ")
c_str = input("a = ")


# check_int sprawdzenie czy liczba jest całkowita
if not (check_int(a_str) and check_int(b_str) and check_int(c_str)):
    
    print("The numbers a, b and c neet to int!")
    
else:
    
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)


    if a == 0:
    
        print("a cannot be 0")
        
    else:
            
        delta = b**2 - 4 * a * c
            
        if delta < 0:
                
            print("there is no solution")
                
        elif delta == 0:
                
            x1 = -b/(2*a)
            print("there is one solution: %.2f" % (x1))
                
        else:
              
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            y1 = a * x1 + b * x1 + c
            y2 = a * x2 + b * x2 + c
            
            print("there are two solutions: %.2f and %.2f" % (x1,x2))
                






















