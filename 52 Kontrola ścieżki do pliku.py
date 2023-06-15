# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 08:05:54 2023

@author: mateu
"""



import os

'''
fileIsOk = False

# bedziemy tak dlugo robic petle dopuki zmienna fileIsOk nie bedzie true 
while not fileIsOk:

    filename = input("Enter path to results file: ")
    
    if os.path.isfile((filename)):
        fileIsOk = True
'''        


# drugi sposob wykonania petli, wykonujemy ja tak dlugo az zostanie przerwana

while True:
    
    filename = input("Enter path to results file: ")
    
    # gdy warunek spawdzajacy bedzie poprawny break przerywa dzialanie petli
    if os.path.isfile((filename)):
        break
    else:
        print("File name is not correct, try again!")



    
print("The results file is %s " % (filename))
 








'''
Tym razem otrzymujesz zadanie zautomatyzowania pobierania danych dotyczących zamówień kierowanych z aptek
 do dystrybutora leków. Zamówienia są przesyłane w postaci plików CSV  i umieszczane w katalogu 
 c:\temp\data_input. Pliki są tam umieszczane przez różne inne procesy w ciągu całego dnia. Codziennie 
 o godzinie 19:00 będzie uruchamiany skrypt, który przeniesie te pliki do innego folderu, 
 np c::\temp\yyyy-mm-dd (gdzie yyyy to rok, mm to miesiąc, a dd to dzień z daty dzisiejszej). 
 Potem na tych plikach są wykonywane dalsze operacje, jak np. import danych.
'''


import os
import datetime

data_input_catalog  = r'c:\temp\data_input'
data_output_catalog = r'c:\temp\data_output'

today = datetime.date.today()
today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d") )


# checking catalog

# input catalog must exists
is_input_catalog_ok = os.path.isdir(data_input_catalog)

# output catalog must exists
is_output_catalog_ok = os.path.isdir(data_output_catalog)


# today output catalog cannot exists                
# w celu przeniesienia kontunuacji kodu do nastepnej lini na koncu trzeba uzyc \
is_today_output_catalog_ok = not (os.path.isdir(today_output_catalog)) and \
                             not (os.path.isfile(today_output_catalog))


if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    
    print("Conditions met! We cen continue!")
    
else:
    
    print('Prerequisites not met! Check the paths!')
    
    if not is_input_catalog_ok:
        print("Input catalog %s must exist!" % (data_input_catalog))
        
    elif not is_output_catalog_ok:
        print("Output catalog %s must exist!" % (data_output_catalog))
        
    elif not is_today_output_catalog_ok:
        print("Today's output %s cannot exist (neither as file nor as directory)!" % (today_output_catalog))
        
            
















