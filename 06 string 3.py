# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 15:01:28 2023

@author: mateu
"""

liczbaJakoTekst = ("1000")
print(liczbaJakoTekst)

# zamiana tupu tekst na liczbe w celu dodania do tekstu jako liczba liczby
x = int(liczbaJakoTekst)+1

print(x)

# type() sprawdza jakiego typu są dane
type(liczbaJakoTekst)
# tu po konwersji na int typ całej zmiennej jest już int
type(int(liczbaJakoTekst)+1)



zmienna = '''
This article is about the comedy group. For their TV show frequently called Monty Python, see Monty Python's Flying Circus.
"Pythonesque" redirects here. For the play by Roy Smiles, see Pythonesque (play).
"The Pythons" redirects here. For the documentary film about the group, see The Pythons (film).
'''

print(zmienna.upper())
print(zmienna.lower().replace('monty', 'flying'))
print(zmienna.split(' '))
print('word python appears',zmienna.lower().count('python'),'times')                        

tekst = "to print the \ you need to put \ twice in your text like this: \\"


print(tekst.replace("\\", "\\\\"))


print("The best hits of '80s!!!")
print('The best hits of \'80s!!!')



amountPLN  = 234
print('cur','\texchange','amount')
print('USD',"\t",3.65,"\t",amountPLN/3.65)
print('EUR','\t',4.23,"\t",amountPLN/4.23)

ValueAsText  = '123.45'
factor = 1.23

print('value is  123.45 factor is 1.23 value*factor= ', float(ValueAsText) * factor)





















