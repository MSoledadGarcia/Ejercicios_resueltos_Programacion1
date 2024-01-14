# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:03:23 2022

@author: maria
"""
#Ejercicio 7.11: Búsqueda binaria

def donde_insertar(lista, x):
    '''Recibe una lista ordenada y un elemento y
    devuelva la posición de ese elemento (si se encuentra en
    la lista) o la posición donde se podría insertar el elemento
    para que la lista permanezca ordenada (si no está en la lista)
    '''
    
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
       
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if pos == -1:
        izq = 0
        der = len(lista) - 1
        while izq <= der:
            medio = (izq + der) // 2
            if lista[medio] > x and lista [medio-1] < x:
                pos = medio 
                break
            if lista[medio] < x and lista[medio] == lista[len(lista)-1]:
                pos = medio +1
                break
            if lista[medio] < x and lista [medio + 1] > x:
                pos = medio +1
                break
            
            if lista[medio] > x and lista[medio -1] > x:
                der = medio - 1
            
            if lista[medio] < x and lista[medio +1] < x:
                izq = medio +1 
        
   
    return pos
   

    
donde_insertar([0,2,4,6], 3)
donde_insertar([0,2,4,6], 4)
donde_insertar([1,2,3], 4)
donde_insertar([1,2,3], 0)

#%%
#Ejercicio 7.12: Insertar un elemento en una lista

def insertar(lista, x):
    posicion = donde_insertar(lista, x)
    
    if posicion > len(lista) -1:
        lista.insert(len(lista), x)
    if lista[posicion] != x and posicion <= len(lista)-1 and posicion != -1:
        lista.insert(posicion, x)
    if posicion == -1:
        lista.insert(0,x)
        
    return posicion


lista = [1, 2, 3]
insertar(lista, 2)
print(lista)
insertar(lista, 4)
print(lista)

    
    