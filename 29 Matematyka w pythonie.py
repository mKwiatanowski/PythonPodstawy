# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 15:10:59 2023

@author: mateu
"""


# dla przypomnienia format float 
f_smaller   = 3.141592653589793
f_bigger    = 3.87756392764


print(f_smaller,f_bigger)
print("\n")


# rzutowanie licz na format int
print(int(f_smaller),int(f_bigger))
print("\n")


# abs wartosc bezwzgledna
print(abs(f_smaller), abs(-f_smaller))
print("\n")


# round zaokraglenie, ktoro stara sie zaokraglac matematycznie czyli cos co jest wieksze badz rowne 5 to zaokragla
# to do gory, a jesli mniejsze to w dol
print(round(f_smaller,2),round(f_bigger,2),round(f_bigger,3))
print("\n")



print(min(f_smaller,f_bigger, max(f_smaller,f_bigger)))
print("\n")



list = [1,2,3,4,5,4,4,5,4]

# w standardzie nie ma funkcji ktora wyliczy srednia, w tym celu trzeba do sesji zaimportowac odpowiedni dodatek
# ale mozna to obejsc liczac sume i ilosc elementow na liscie
print(sum(list), len(list))
print("\n")

print(sum(list)/len(list))
print("\n")



# przyklad w ktorym tym float dziala w sposob nie intuicyjny
# spodziewanym wynikiem powinna byc liczba 2.68
# tym float nie jest precyzyjny, trzeba pamietac ze to nie bug tylko specyfika typu float
# defakto mozna tu traktowac 2.675 == 264999999....
print(round(2.675,2))






percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
           8.740978348,6.174819567]
 
countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
             'Norway', 'Portugal','United Kingdom','Serbia','Germany','Albania',
             'France','Czech Republic','Denmark','Australia','Finland','Bulgaria',
             'Moldova','Sweden','Hungary','Israel','Netherlands','Ireland',
             'Cyprus','Italy']


sumOfPoints = 4988



print("najnizsza wartosc :", min(percent), "najwyższa wartosc :", max(percent))


for per in range(len(percent)):
    print("wartosc :", percent[per], "\t", int(percent[per]), "\t", round(percent[per],2), "\t",  int(round(percent[per]*sumOfPoints/100,0)) ,
         "\t",  countries[per])
    











