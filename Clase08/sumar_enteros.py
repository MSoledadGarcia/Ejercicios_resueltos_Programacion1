# -*- coding: utf-8 -*-

def sumar_enteros(desde, hasta):
    lista = []
    for i in range(desde, hasta + 1):
        lista.append(i)
    suma = 0 #invariante
    for e in lista:
        suma += e #invariante
    return suma 



sumatoria = sumar_enteros(5,9)
print(sumatoria)

#Falta def la funcion sin ciclo

#%%
