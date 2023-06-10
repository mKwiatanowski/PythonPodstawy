# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 13:56:20 2023

@author: mateu
"""

text ="to jest tekst."
text.endswith('st.')  # sprawdzenie czy tekst kończy się znakami st.

text.islower() #sprawdzenie czy tekst jest zapisany małymi literami
text.upper()  # zmiana tekstu na duże litery
text.upper().isupper() #najpierw upper zmienia tekst na duże litery 
                        #nastepnie sprawdzam czy tekst jest zapisany dużymu literami
                        
                        
text.find('st') # wyszukanie w tekscie znaków st i zwrócenie na którym
                #znaku się zaczyna python liczy od 0
text.find('st',4) # to samo co wyżej tylko zaczynamy liczyć od 4 znaku 

text.replace('o', '0').replace('e', '3') #replace zmiana okslonego znaku na inny

text.split(' ') #split może podzielić tekst wynikiem jest tabela, w którym każdym elementem
                #jest odzielne słowo z tekstu
                
                
wygladaJakLiczba = '1000'
wygladaJakLiczba.isdigit()  #sprawdza czy napis wyglada jak liczba
wygladaJakLiczba.isdecimal() #sprawdza czy napis jest liczba z przecinkiem
wygladaJakLiczba.isalpha() #sprawdza czy są same litery   
wygladaJakLiczba.isalnum() #sprawdza czy tekst to litery i liczby             
                