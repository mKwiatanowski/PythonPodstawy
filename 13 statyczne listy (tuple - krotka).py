# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 09:39:47 2023

@author: mateu
"""

# róż☺nica między tuple a lista jest taka że tu uzywa sie nawias () a tam nawias []
Tax = (4, 7, 8, 23)

# odwolanie do indexu
print(Tax[2])

# ze znakiem - mozna indexowac od konca (tutaj 0 nie jest pierwsze ( ostatnia pozycja ) a -1 )
print(Tax[-1])

# na ktorej pozycji znajduje sie szukana wartosc
print(Tax.index(7))

# sprawdzenie ile razy wystepuje dany index
print(Tax.count(8))

# maksymalna wartosc
print(max(Tax))


# nie można modyfikowac tej listy jak listy tekstowej uzywajac metod revers() insert() sort() itp
# zeby moc modyfikowac liste puple nalezy ja przeksztalcic w liste 
# co skutkuje tym ze nawiasy okragle zamieniaja sie na kwadratowe
TaxList = list(Tax)

# dodanie do nowej listy nowa wartosc
TaxList.append(30)

# ponowa zamiana listy na liste tuple
# uzywajac listy tuple nalezy pamietac ze nic w niej nie mozna zmienic ten typ listy jest niezmienny
# jesli jest koniecznosc modyfikacji nalezy zamienic tuple na liste zrobic modyfikacje i ponownie zamienic na tuple
NewTax = tuple(TaxList)



print(Tax)
print(TaxList)
print(NewTax)

# z listy tuple przypisanie wartosci listy do osobnych zmiennych
# w locie przypisalismy do nowego taple tax1, tax2... z istniejacego juz tax
(tax1, tax2, tax3, tax4) = Tax
print(tax1,tax2,tax3,tax4)

a = 1
b = 10
print("a = ",a, "\tb = ",b)

# jesli jest koniecznosc zamiany wartosci miedzy zmiennymi czyli 
# a = b i b = a
# w poniższym przykladzie gdy do a przypiszemy b to gdy do b chcemy przypisac a to przypiszemy juz zmienione a
# a = b
# b = a
# print("a = ",a, "\tb = ",b)

# nalezy zrobic nastepujacy tip zeby do b przypisac stare a nalezy zapisac dodatkowa zmienna ktora przechowa 
# stara wartosc a
# temp = a
# a = b
# b = temp

# jednak prostrzym rozwiazaniem jest zapisac wartosci zmiennych do tuple i zeby python zamienil wartosci w tle
# w takim przypadku nie trzeba tworzyc dodatkowej zmiennej temp
(a, b) = (b, a)

print("a = ",a, "\tb = ",b)



marketing = ["loyality program", "client promotion", "market research"]

# dodanie do listy nowej pozycji apped( zawsze na koncu )
marketing.append("public relations")

# wyswietlenie 3 pozycji na liscie
print(marketing[2])

# wstawienie na 2 pozycji nowego elementu
marketing.insert(1, "investor relations")

# kopiowanie listy do nowej listy
emailMarketing = marketing.copy()

# sortowanie listy
emailMarketing.sort()

# dodanie nowej listy do istniejacej listy
internalEmails = ["internal communication"]
emailMarketing.extend(internalEmails)

# utworzenie listy tuple z wartosciami listy
newTuple = tuple(emailMarketing)
print(newTuple)





print(marketing)
print(emailMarketing)
print(internalEmails)




































