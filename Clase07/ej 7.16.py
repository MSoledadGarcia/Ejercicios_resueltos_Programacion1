# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 23:25:04 2022

@author: maria
"""


def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
busqueda_binaria(lista, 5, verbose = True)
#%%

#7.6 Gráficos de complejidad

def busqueda_secuencial_comps(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
busqueda_secuencial_comps(lista, 7)[0]
busqueda_secuencial_comps(lista, 7)[1]

#%%
#Ejercicio 7.16: Contar comparaciones en la búsqueda binaria

def busqueda_binaria_comps(lista, x):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    Devuelve la cantidad de comparaciones que realizo el 
    algoritmo
    '''
    comps = 0
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        comps += 1
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            #break
        #comps += 1    
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
            
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
            
    return pos, comps


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
busqueda_binaria_comps(lista, 5)
busqueda_binaria_comps(lista, 6)
#%%

import random

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)

m = 10000
n = 100
lista = generar_lista(n, m)

# acá comienza el experimento
x = generar_elemento(m)
comps = busqueda_secuencial_comps(lista, x)[1]


m = 10000
n = 100
k = 1000
lista = generar_lista(n, m)

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_comps(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom


#%%
import matplotlib.pyplot as plt
import numpy as np

m = 10000
k = 1000

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos,comps_promedio,label = 'Búsqueda Secuencial')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()
plt.show()