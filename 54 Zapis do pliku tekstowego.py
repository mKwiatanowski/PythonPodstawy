# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 09:48:27 2023

@author: mateu
"""



filename = r"c:\temp\output.txt"

line = "Europe"

cities = ["London", "Berlin","Paris","Warsow","Madrid","Rome"]

# parametr "w" czyli write zapisywanie, trzeba pamietac ze jednoczenie powoduje to wyczyszczenie poprzedniej zawartosci
# pliku
# parametr "a" append sluzy do dopisania czegos nowego do pliku zachowujac to co bylo w nim do tej pory
# parametr "w+" oznacza ze plik bedzi otwarty i do zapisu i do odczytu z czyszczeniem jego zawartosci
# parametr "a+" otwarcie pliku do odczy i do zapisu nie czyszczac zawartosci pliku
# parametr "r" do odczytu bez mozliwosci modyfikacji i zapisu
file = open(filename, 'a')

# metoda write(co ma byc zapisane) zapisuje wartosc zmiennej do pliku
file.write(line)

# writelines() metoda ktora zapisuje liste do pliku
file.write("\n")
#file.writelines(cities)

for city in cities:
    file.write(city+'\n')

file.close()








'''
W tym zadaniu napiszesz program, który zapyta użytkownika o adresy www i zapisze je w pliku.
'''


import os

webaddresses = []

line = input("Wprowadz nazwe strony www: ")


while line != '':
    webaddresses.append(line)
    line = input("Wprowadz kolejna nazwe strony www lub nacisnij enter aby zakonczyc: ")


print(webaddresses)

# zwrocenie biezacej sciezki 
dirname = os.getcwd()
# wprowadzenie nazwy pliku
filename = input("Wprowadz nazwe pliku ")
# polaczenie sciezki i nazwy pliku
filepath = os.path.join(dirname, filename)
# otwarcie pliku w sciezce
file = open(filepath,"w+")

for web in webaddresses:
    file.write(web+"\n")

file.close()




'''
W tym zadaniu wczytasz i przeanalizujesz plik utworzony w poprzednim zadaniu
'''


import os

filename = input("Wprowadz sciezke do pliku: ")


while not os.path.isfile(filename):
    print("Wrowadzono niepoprawna sicezke do pliku")
    filename = input("Wprowadz sciezke do pliku ")
    
webaddresses=[]

with open(filename,"r") as file:
    
    for line in file:
        
        webaddresses.append(line.replace('\n',''))

    file.close()


for line in webaddresses:
    
    # funkcja endswith(szukaj) oznacza ze szukamy parametr od konca tekstu
    if line.endswith("pl"):
        print("Adres %s jest adresem z Polski" % line)    

    else:
        print("Adres %s nie jest adresem z Polski" % line) 



# modyfikuj zadanie 2 



import os

filename = input("Wprowadz sciezke do pliku: ")

while not os.path.isfile(filename):
    print("Wrowadzono niepoprawna sicezke do pliku")
    filename = input("Wprowadz sciezke do pliku ")
    
webaddresses=[]

with open(filename,"r") as file:
    
    for line in file:
        
        webaddresses.append(line.replace('\n',''))

# zwrocenie sciezki bez nazwy pliku
dirname = os.path.dirname(filename)

webadress_pl    = os.path.join(dirname, "webs_pl.txt")
webadress_other = os.path.join(dirname, "webs_other.txt")


filePl      = open(webadress_pl,'w')
fileOther   = open(webadress_other, 'w')


for line in webaddresses:
    if line.endswith('pl'):
        filePl.write(line + '\n')
    else:
        fileOther.write((line + '\n'))


filePl.close()
fileOther.close()



























