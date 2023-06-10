# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 17:47:21 2023

@author: mateu
"""

# %s pozwala w princie wstawić dowolny tekst
message1 = 'Processing file %s'
print(message1 % ('file_1.txt'))

# %d pozwala wstawić dowolną liczbę
message2 = 'File %s has size %d KB'
print(message2 % ('file_2.txt',100))

# liczba pomiedzu % a s/d wskazuje maksymalną ilosc znakow jaka mozna wstawic 
# (jesli nie wykorzysta sie zalozonej ilosci znakow to miejsce na te znaki zostanie zarezerwowoane)
message3 = 'File %20s has size %10d KB'
print(message3 % ('file_3.txt', 100))


# używamy nawiasu klamrowego {liczba : s} jesli jest 0 to spodziewamy sie dokładnie jednego
# parametru i s oznacza ze ten parametr ma byc napisem 
message4 = 'Processing file {0:s}'
print(message4.format('filel.txt'))


# 0 jest zarezerwowane dla napisu 1 jest zarezerwowane dla liczby jest to pozycja 
# w funkcji format (0,1)
message5 = 'File {0:s} has size {1:d}'
print(message5.format('files.txt', 155))

# można w tym przykładzie zamienić kolejnosc
message6 = 'File {1:s} has size {0:d}'
print(message6.format(222, 'files.txt'))

# liczba przed s i d oznacza długossc spodziewanej ilosci znakow to samo co wyzej
message7 = 'File {1:20s} has size {0:10d}'
print(message7.format(741, 'files.txt'))


# jesli uzywamy %s %d to wywolujac zmienna nalezy po zmiennej dac % i w ( wprowadzic dane )
helloMessage1  = "Hello %s !"
print(helloMessage1 %('Kate'))
print(helloMessage1 %('Cris'))


# jesli uzywamy {0:s} {0:d} to wywolujac zmienna nalezy po zmiennej dac .format i w ( wprowadzic dane )
helloMessage2  = "Hello {0:s} !"
print(helloMessage2.format('Kate'))
print(helloMessage2.format('Cris'))

helloMessage3 = "%s has %d %s"
print(helloMessage3 % ('Kate' , 1 , 'animal'))
print(helloMessage3 % ('Cris' , 10000 , '$'))

helloMessage4 = "{0:s} has {1:d} {2:s}"
print(helloMessage4.format('Kate', 1, 'animal'))
print(helloMessage4.format('Cris', 10000, '$'))


line = "{0:d} {1:20s} costs {2:6d} €"
print(line.format(1,'Ice cream', 3))
print(line.format(2,'Trip to Venice', 119))
print(line.format(3,'Pizza Hawaii', 6))






































