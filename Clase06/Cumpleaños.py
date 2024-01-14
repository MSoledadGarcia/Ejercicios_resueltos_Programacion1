# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 17:31:41 2022

@author: maria
"""
import random

#%%
#Ejercicio 6.3: Cocumpleaños


def cumple():
    cumpleanios = []
    for i in range(23):
        cumpleanios.append(random.randint(1,365))
    return cumpleanios


cumple()

def cumplen_igual(cumpleanios):
    if len(cumpleanios) == len(set(cumpleanios)):
        return False
    else:
        return True


cumplen = cumplen_igual(cumple())
cumplen
    


N = 10000
C = sum([cumplen_igual(cumple()) for i in range(N)])
C
prob = C/N
prob

print(f'Para que la probabilidad de que dos personas cumplan años el mismo día sea mayor a 0,5 debe haber un grupo de 23 personas')









#FALTA ULTIMA PARTE