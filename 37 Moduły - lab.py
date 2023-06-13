# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 08:57:07 2023

@author: mateu
"""



# podsumowanie


inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]


import math


print("W liscie inputdata znajduje sie %d elementow, natomiast w liscie factorytable znajduje sie %d elementow" 
      % (len(inputdata),len(factortable)))


if len(inputdata) == len(factortable):
    i = 0
    while i <len(inputdata):
        minvalue = inputdata[i] - factortable[i] * inputdata[i]
        maxvalue = inputdata[i] + factortable[i] * inputdata[i]
        
        
        print('minvalue=',minvalue,'maxvalue=',maxvalue)
        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
    
        print(mininteger,"\t",inputdata[i],"\t",maxinteger)   
        i += 1
    
    print("ok")
else:
    print("inputdata and factortable need to have equal number of elements")





import random



i = 0
while i <len(inputdata):
   minvalue = inputdata[i] - random.random() * inputdata[i]
   maxvalue = inputdata[i] + random.random() * inputdata[i]
        
        
   print('minvalue=',minvalue,'maxvalue=',maxvalue)
   mininteger = math.floor(minvalue)
   maxinteger = math.ceil(maxvalue)
    
   print(mininteger,"\t",inputdata[i],"\t",maxinteger)   
   i += 1
    
print("ok")





import datetime

print("Today is: ",datetime.date.today())
print("Today is format yyyy-mm-dd ", datetime.date.today().strftime("%Y-%m-%d"))




















































