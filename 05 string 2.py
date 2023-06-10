# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 14:51:08 2023

@author: mateu
"""

drive = 'C:\\'
folder = 'scripts\\python\\'
file = 'myscript.py'
patch = drive + folder + file
print(patch)

justText = r'test with\nnewline' #dodanie r przed tekst spowoduje, ze tekst jest 
                                #trakowany jako surowy tekst
print (justText)