# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 08:47:20 2023

@author: mateu
"""



# open("","r") obsluguje czytanie plikow, jednak trzeba pamietac ze parametr jaki przekazuje sie jest w "" i nalezy
# uzywac podwojnego \\ w celu oddzielenia katalogow sciezki, natomiast drugi parametr odpowiada za tym odczytu pliku
# " r " oznacza read czyli ten plik bedzie mozna tylko odczytac be zmozliwosci dokonania zmian
file = open("C:\\temp\\joke.txt","r")


# metoda read() pozwala w calosci zaczytac zawartosc pliku
content = file.read()
print(content)

# bardzo istotne, jesli jakis plik sie otworzylo to nalezy go pozniej zamknac
# close() slozy do zamkniecia otwartego pliku
file.close()


# powyższy zapis jest nie do konca dobry, poniewaz trzeba pamietac o zamknieciu pliku
# jednak mozna to zrobic na inny sposob


# ta instrukcja jest odpowiednia do przeczytania malych pliku, jednak przy duzych plikach
# to rozwiazanie bedzie niewydajne
with open("C:\\temp\\joke.txt","r") as file:
    content = file.read()
    print(content)


with open("C:\\temp\\joke.txt","r") as file:
    # za pomoca petli mozna pobierac i wyswietlac kazda linijke z pliku oddzielnie
    # takie rozwiazanie jest lepsze pod wzgledme wydajnosci
    for line in file:
        print(line)
    
    



# !!! UWAGA !!! tego nie należy robić !!!

# po otwariu pliku otworzylismy petle ktora czyta wszystkie linie z pliku pokolei, metoda readlines() wczytuje 
# naraz caly plik do pamieci i nastepnie ten plik dzieli linijkami na kolekcje napisów czyli w tym przypadku
# mamy doczynienia z pamieciowa reprezentacja plikow w formie linijek
file = open("C:\\temp\\joke.txt","r")
for line in file.readlines():
    print(line)
    
file.close()



file = open("C:\\temp\\joke.txt","r")

# metoda read(x) oznacza, ze na raz chcemy przeczytac 10 bitow z tego pliku
fragment = file.read(10)

# nastepnie zeby przejsc przez caly plik nalezy napisac petle ktora bedzie przetwazac ten plik w paczkach po 10 bitow
while fragment:
    # tell() metoda ktora wskazuje gdzie w tej chwilie znajduje sie wskaznik
    print(file.tell(), fragment)
    # po przeczytaniu poprzednich 10 mitow, otwieramy kolejne 10 bitow i wczytujemy do petli, jesli nic wiecej nie bedzie
    # petla zakonczy sie
    fragment = file.read(10)
    
file.close()






'''
Naszym zadaniem jest przeczytać ten plik i przetwarzać go linijka po linijce. Zamówienie umieszczone 
w każdej linii składa się z 3 informacji: nazwa apteki, nazwa leku, ilość opakowań leku. Zdarza się, 
że niektóre zamówienia nie są poprawne i zawierają więcej danych - tutaj wiersz 2. W tym zadaniu 
przetwarzamy ten plik zupełnie ręcznie, ale oczywiście istnieją zdecydowanie lepsze metody na przetwarzanie 
danych w Pythonie, np. biblioteka PANDAS, której poświęciłem inny kurs.
'''


file_path = r'c:\temp\data_input\orders.csv'

with open(file_path,"r") as file:
    
    for line in file:
        
        line = line.replace("\n", '')
        order = line.split(",")
        
        if len(order) == 3:
            print("Order from drugstore %s, item %s, amount %s" % (order[0], order[1], order[2]))
            
        else:
            print("Line %s malformed!!!" % (line))
        
    
print("Processing finished")



























