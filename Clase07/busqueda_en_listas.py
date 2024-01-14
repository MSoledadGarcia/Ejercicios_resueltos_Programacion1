# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 10:02:12 2022

@author: maria
"""

# Ejercicio 5.3:  Búsquedas de un elemento

def buscar_u_elemento(lista, e):
    pos = -1  
    for i, z in enumerate(lista):  
        if z == e:
            pos = i 
            #break
    return pos

def buscar_n_elemento(lista, e): 
    cant = 0
    for i, z in enumerate(lista):  
        if z == e:
            cant += 1
            #pos = i 
            #break
    return cant


posicion_elemento = buscar_u_elemento([1,2,3,2,3,4],1)
posicion_elemento
posicion_elemento2 = buscar_u_elemento([1,2,3,2,3,4],2)
posicion_elemento2

cantidad_elemento = buscar_n_elemento([1,2,3,2,3,4],3)
cantidad_elemento
cantidad_elemento2 = buscar_n_elemento([1,2,3,2,3,4],5)
cantidad_elemento2

#%%
#Ejercicio 5.4: Búsqueda de máximo y mínimo


def maximo(lista):
    m = lista[0]  #toma el primer indice de la lista y el if compara y se queda con el >
    for e in lista:
        if e > m:
            m = e
    return m

maximo([1,2,7,2,3,4])
maximo([1,2,3,4])
maximo([-5,4])
maximo([-5,-4])


def minimo(lista):
    m = lista[0]
    for e in lista:
        if e < m:
            m = e
    return m


minimo([1,2,7,2,3,4])
minimo([1,2,3,4])
minimo([-5,4])
minimo([-5,-4])




