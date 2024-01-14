# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 19:56:12 2022

@author: maria
"""
import random
import numpy as np 
    
def medir_temp(n):
    mediciones = []
    for i in range(n):
        mediciones.append(random.normalvariate(37.5,0.2))
    return mediciones

medicion_array= np.array(medir_temp(999))
np.save('../Data/temperaturas.npy', medicion_array)



def resumen_temp(n):
    temperaturas = medir_temp(n)
    temp_max = max(temperaturas)
    temp_min = min(temperaturas)
    promedio = sum(temperaturas)/n
    lista = sorted(temperaturas)
    mitad = len(lista)//2
    mediana = 0.0
    if len(temperaturas) %2 == 0:
        mediana =  (lista[mitad - 1]+ lista[mitad])/2
            
    if len(temperaturas) % 2 != 0:
        mediana = lista[mitad]
        
    return f'Temperatura máxima: {temp_max:.2f} Temperatura mínima: {temp_min:.2f} Temperatura promedio: {promedio:.2f} Mediana: {mediana:.2f}'
   
 
temperatura = resumen_temp(999)
print(temperatura)








