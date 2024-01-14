# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 12:05:25 2022

@author: maria
"""
#Ejercicio 5.5: Invertir una lista


def invertir_lista(lista):
    invertida = []
    
    for e in lista:
        invertida.insert(0, e)
      
    return invertida    


invertir_lista([1, 2, 3, 4, 5])
invertir_lista( ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])

#%%
def invertir_lista(lista):
    invertida = []
    
    for e in lista:
        invertida = [e] + invertida
      
    return invertida    


invertir_lista([1, 2, 3, 4, 5])