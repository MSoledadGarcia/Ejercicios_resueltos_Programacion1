# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 09:57:29 2022

@author: maria
"""

import os

os.getcwd()
#%%    
print("  ", end="")
for i in range(10):
    
    print(f'{i:>3}', end="")
print()
s = "-"
print(f' {s:->31s}')
for x in range(10):
    valor = 0
    print()
    print(f'{x:>2}:', end="")
    for y in range(10):
        
        print(f'{valor:>2}', end=" ")
        valor = valor + x
        
        