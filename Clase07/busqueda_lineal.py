# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 09:49:02 2022

@author: maria
"""


def busqueda_lineal_lordenada(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.Con una lista ordenada.  
    '''
    pos = -1  # comenzamos suponiendo que e no está 
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break
        if z > e:
            pos = -1
            break    # y salimos del ciclo
            
    return pos



busqueda_lineal_lordenada([1,3,5,7,24,32,56,76], 32)
busqueda_lineal_lordenada([1, 4, 54, 3, 0, -1], 3)

busqueda_lineal_lordenada([1, 4, 54, 3, 0, -1], 0)

busqueda_lineal_lordenada([], 42)