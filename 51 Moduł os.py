# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 15:04:36 2023

@author: mateu
"""



import os
import time

# os.getcwd() zwraca informacje o biezacym katalogu
print("Current directory is:", os.getcwd())

currentDir = os.getcwd()
filename = "result.txt"

# os.path.join() sluzy do polaczenia sciezki dostepowej i nazwy pliku w celu utworzenia kompletnej sciezki do pliku
fullpath = os.path.join(currentDir, filename)
print("\nThe constructed file path is: ", fullpath)



# os.path.abspath() sprawdz do jakiej sciezki moglby byc zapisany plik gdzie jako parametr przyjmuje jego nazwe
relativePath = "cutput.txt"
print("\nThe absolute path is: ", os.path.abspath(relativePath))


filepath = r"c:\temp\results.txt"

# os.path.basename() majac cala sciezke do pliku zwroci tylko nazwe pliku, jako parametr pelna sciezka
print("\nThe file name part is: ", os.path.basename(filepath))
# os.path.dirname(filepath) majac cala sciezke do pliku zwroci tylko sciezke usuwajac nazwe pliku jako parametr sciezka
print("The directory part is: ", os.path.dirname(filepath))
# os.path.exists() sprawdzenie czy plik lub folder istnieja parametr przekazywany to podana sciezka
print("\nIs file existing? ", os.path.exists(filepath))



if os.path.exists(filepath):
    # os.path.getmtime() data i czas modyfikacji pliku
    # os.path.getctime() data i czas dla utworzenia
    # os.path.getatime() data i czas dla ostatniego dostepu
    # minusem tego jest to ze python przedstawi czas w sekundach od poczatku siwata w pythonie
    # mozna uzyc modulu time i funkcji time.localtime i dane te beda bardziej przystepne
    print("\nLast modify date is: ", os.path.getmtime(filepath))
    print("Last modify date is: ", time.localtime(os.path.getmtime(filepath)))

    # os.path.getsize() pobranie informacji o rozmiarze pliku rozmiar wzracany jest w bitach
    print("\nFile size is: ", os.path.getsize(filepath))

    # os.path.isfile() sprawdzenie czy sciezka identyfikuje plik
    print("\nIs it a file? ", os.path.isfile(filepath))
    # os.path.isdir() sprawdzenie czy sciezka identyfikuje katalog
    print("Only file name part:", os.path.isdir(filepath))
    
    # os.path.split() podzieli sciezke do pliku na dwie czesci jedna bedzie sama sciezka do katalogu a druga to nazwa pliku
    print("\nPath splitted: ", os.path.split(filepath))
    # s.path.split(filepath)[x] wyswietlenie ktory z elementow tuple ma zostac wyswietlony  
    print("Onli file name part: ", os.path.split(filepath)[1])
    
    # os.path.splitdrive() podzieli sciezke na 2 elementy 1 to wycieta nazwa dysku, a 2 to pozostala sciezka
    print("\nPath splitted into drive: ", os.path.splitdrive(filepath))
    # os.path.splitdrive(filepath)[x]) z wycietej sciezki jak wyzej x deklaruje ktora wartosc ma wyswietlic
    print("Onli drive: ", os.path.splitdrive(filepath)[0])






dir_str = input("Wprowadx sciezke do pliku: ")

if not os.path.exists(dir_str):
    
    print("Podana scieżka jest błędna")

else:
    
    file = input("Wprowadz nazwe pliku: ")
    path = os.path.join(dir_str, file)
    
    if not os.path.exists(path):
        
        print("Plik w sciezce %s nie istnieje" % (path))
    
    
    else:
        
        print("Informacje o pliku: \n")
        print("Data ostatniej modyfikacji: ", os.path.getmtime(path))
        print("Rozmiar w bajtach: ", os.path.getsize(path))
        print("Biezaca sciezka: ", os.getcwd())
        # os.path.relpath() zwraca wzgledna sciezke do pliku ( bez literki dysku )
        print("Sciezka do pliku: ", os.path.relpath(path))























