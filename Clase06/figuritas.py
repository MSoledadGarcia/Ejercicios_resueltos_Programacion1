# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 19:54:30 2022

@author: maria
"""

import random
import numpy as np
import matplotlib.pyplot as plt
#Ejercicio 6.13: Crear

def crear_album(figus_total):
    album = np.zeros(figus_total)
    return album
#%%
#Ejercicio 6.14: Incompleto
def album_incompleto(A): # A = nombre del album creado
    if 0 in A:
        return True
    else:
        return False
#%%
#Ejercicio 6.15: Comprar
def comprar_figus(figus_total):
    figuritas = random.randint(1,figus_total)
    return figuritas
#%%

'''
def llenado_de_album(cant_figus, nombre_album):
    for i in cant_figus:
        nombre_album[i - 1] += 1
    return nombre_album'''

'''def album_lleno(nombre_album, cant_figus):
    llenado = album_incompleto(nombre_album)
   
    cantidad = 0
    
    while llenado == True:
        figu = figuritas(cant_figus)
        completar = llenado_de_album(figu, nombre_album)
        cantidad += 1
        llenado = album_incompleto(completar)
        
    return cantidad'''

#%%

#Ejercicio 6.16: Cantidad de compras

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    llenado = True
    cantidad = 0
    while llenado == True:
        figu = comprar_figus(figus_total)
        album[figu - 1] += 1
        cantidad +=1
        llenado = album_incompleto(album)
    return cantidad
            
completar_album = cuantas_figus(670)
print(f' Para completar un album de a una figurita aleatoria, necesito comprar {completar_album} figuritas')
print()

#%%
#Ejercicio 6.17



n_repeticiones = 1000
promedio = np.mean([cuantas_figus(6) for i in range(n_repeticiones)])
print(f'Para completar un album de 6 figuritas hay que comprar un promedio de {promedio:.0f} figuritas.')
print()

#%%
#Ejercicio 6.18:
def experimento_figus(n_repeticiones, figus_total):  
    cantidad = np.mean([cuantas_figus(figus_total) for i in range(n_repeticiones)])
    return cantidad

album_100_670 = experimento_figus(100, 670)
print(f'Para completar un album de 670 figuritas hay que comprar en promedio unas {album_100_670:.0f}')

#%%
#Ejercicio 6.19:
    
paquete=[]
for i in range(5):
    paquete.append(random.randint(1,670))
#print(paquete)

#%%
#Ejercicio 6.20:
     
def comprar_paquete(figus_total, figus_paquete):
    paquete=[]
    for i in range(figus_paquete):
        paquete.append(random.randint(1,figus_total))
    return paquete  


#%%
#Ejercicio 6.21:

def cuantos_paquetes(figus_total, figus_paquete):
    
    album = crear_album(figus_total)
    llenado = True
    cantidad = 0
    while llenado == True:
        paquete = comprar_paquete(figus_total, figus_paquete)
        cantidad +=1
        for i in paquete:
            album[i - 1] += 1
            
            llenado = album_incompleto(album)
    return cantidad

cuantos = cuantos_paquetes(670,5)       
print(f'Para completar un album de 670 figuritas hay que comprar {cuantos} paquetes de 5 figuritas')

#%%
#Ejercicio 6.22:

    
n_repeticiones = 100
promedio_paquetes = np.mean([cuantos_paquetes(670,5) for i in range(n_repeticiones)])
print(f'Para completar un album de 670 figuritas se necesitan un promedio de {promedio_paquetes:.0f} paquetes de 5 figuritas')
print()

'''promedio_paquetes_qatar = np.mean([cuantos_paquetes(638,5) for i in range(n_repeticiones)])
print(f'Para completar el album de Qatar 2022, el cual tiene 638 figuritas se necesitarian aproximadamente {promedio_paquetes_qatar:.0f} paquetes de 5 figuritas cada paquete. Teniendo en cuenta que cada paquete sale $150, se necesitan aproximadamente ${promedio_paquetes * 150:.0f}')'''


def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = [i - 1 for i in comprar_paquete(figus_total, figus_paquete)]
        #paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

llenado_de_album = calcular_historia_figus_pegadas(figus_total, figus_paquete)

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()


#%%
#PROBABILIDAD
#Ejercicio 6.23:
n_repeticiones = 100
prueba = [cuantos_paquetes(670,5) for i in range(n_repeticiones)]

lista_figus= []
for i in prueba:
    if i <= 850:
        lista_figus.append(i)
albumes_llenos = len(lista_figus)/n_repeticiones
probabilidad = albumes_llenos*100

print(f' La probabilidad de completar un album de 670 figuritas con 850 paquetes o menos es de {probabilidad:.2f} %')

    


n_paquetes_hasta_llenar=np.array([cuantos_paquetes(670,5) for i in range(n_repeticiones)])
#n_paquetes_hasta_llenar
albumes_llenos2 = (n_paquetes_hasta_llenar <= 850).sum()
probabilidad2 = (albumes_llenos2 / n_repeticiones) *100
print(f' La probabilidad de completar un album de 670 figuritas con 850 paquetes o menos es de {probabilidad2:.2f} %')



#%%
#Ejercicio 6.24: Plotear histograma

def experimento_paquetes(n_repeticiones, figus_total, figus_paquetes):  
    cantidad =[cuantos_paquetes(figus_total, figus_paquetes) for i in range(n_repeticiones)]
    return cantidad


lista_cuantos_paquetes = experimento_paquetes(100,670,5)
#print(lista_cuantos_paquetes)

plt.hist(lista_cuantos_paquetes, bins=5)
plt.show()
plt.xlabel("Cantidad de paquetes")
plt.ylabel("Albumes llenos")
plt.title("Cantidad de paquetes necesarios para completar un album")

#%%
#Ejercicio 6.26: Repetí suponiendo que no hay figuritas repetidas en un paquete. ¿Cuánto cambian las probabilidades?

   
def comprar_paquete2(figus_total, figus_paquete):
    figus = []
    for i in range(1,figus_total+1):
        figus.append(i)
    paquete=[]
    for i in range(figus_paquete):
        #paquete.append(random.randint(1,figus_total))
        paquete.append(random.sample(figus, k=1)[0])
    return paquete  


def cuantos_paquetes2(figus_total, figus_paquete):   
    album = crear_album(figus_total)
    llenado = True
    cantidad = 0
    while llenado == True:
        paquete = comprar_paquete2(figus_total, figus_paquete)
        cantidad +=1
        for i in paquete:
            album[i - 1] += 1  
            llenado = album_incompleto(album)
    return cantidad

def experimento_paquetes2(n_repeticiones, figus_total, figus_paquetes):  
    cantidad = np.mean([cuantos_paquetes2(figus_total, figus_paquetes) for i in range(n_repeticiones)])
    return cantidad


paquetes_sin_repes = cuantos_paquetes2(670,5)       
print(f'Para completar un album de 670 figuritas con paquetes que no tienen repetidas hay que comprar {paquetes_sin_repes} paquetes de 5 figuritas')

print(f' Para completar un album de 670 figuritas se necesitan un promedio de {experimento_paquetes2(100,670,5)} paquetes (sin figus repetidas).')






