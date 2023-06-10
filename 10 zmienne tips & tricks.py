# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 14:29:23 2023

@author: mateu
"""

# W pythonie nie trzeba od razu definiować typu zmiennej, python na podstawie zapisanych danych sam dopasuje jaki to typ 

Title = "Python"
print("Title is ", type(Title))

Version = 3
print("Version is ", type(Version))

Progress = 0.21
print("Progress is ", type(Progress))

# pewne typy są silniejsze, a pewne sa slabsze, np mnożąc int i float wynik w tym wypadku bedzie float
print("This expression is ", type(Progress * Version))

# jesli chcemy zapisac kilka zmiennych o tej samej wartosci nie trzeba zapisywac kazdej osobno

x = 1
y = 1
z = 1

print(x,y,z)

# mozna to zapisac, ze a,b,c sa rowne same sobie i przyjmuja ta sama wartosc
a=b=c=2
print(a,b,c)


# mozna zmienic wartosc dowolnej zmiennej pozniej co bedzie skutkowac tym ze zmiennej zostanie przypisana nowa wartosc
# zapisana w pamieci komputera
c = 3
print(a,b,c)


# wszystko to co sie dzieje w pythonie jest zgodne z zasadami matematycznymi
print(2+2*2)
print(6/2*(1+2)) 

# znakiem ** potegujemy do x**p
print(4**3**2)


# zmienianie wartosci zmiennych liczbowych

x = 1
x + 1 

# wartosc zmiennej to 1 gdy do x + 1 daje to 2, jednak ten zapis nie zmienia sie wartosc zmiennej
x

# logicznie aby zmienic wartosc zmiennej nalezy uzyc zapisu

x = x + 1

x

# poniższy zapis znaczy to samo co x = x + 1 jest jednak nieco krutszy a co za tym idzie nieco szybszy w zapisie
x += 1
x


x -= 1
x






v1 = 126
v2 = '126'
v3 = 126.0
v4 = '126.0'

print("Pyt zmiennej v1 to: ", type(v1))
print("Pyt zmiennej v2 to: ", type(v2))
print("Pyt zmiennej v3 to: ", type(v3))
print("Pyt zmiennej v4 to: ", type(v4))

print("wynik dodawania v1 i v3 ", type(v1+v3))
print("wynik dodawania v2 i v4 ", type(v2+v4))


print( 7-1*0+3+3 )



print(4**5 / 2**3)


print(99+9/9)











