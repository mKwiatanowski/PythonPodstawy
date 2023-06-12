# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 13:46:26 2023

@author: mateu
"""



# tabliczka mnożenia
# pętla zewnętrzna
for x in range(1,6):
    
    # pętla wewnetrzna
    for y in range(1,6):
        print(x, "*", y , "=", x*y)





for x in range(1,6):
    line = str(x)
    
    for y in range(1,6):
        # formatując do prawej strony dla przykładu %3d czyli wyswietlamy 3 liczby
        line += '\t%3d' % (x*y)
    print(line)




# silnia

i = 10
result = 1

for j in range(1,i+1):
    result *= j
    print(j,result)





x = 10


for j in range(1,x+1):
    result = 1
    for x in range(1,j+1):
        result *= j
    
    
    print(j,result)




list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']



for z in list_noun:
    
    for x in list_adj:
        
        
        print(z,x)
































