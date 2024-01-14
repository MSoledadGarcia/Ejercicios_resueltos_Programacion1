# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:08:59 2022

@author: maria
"""

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000


def grafico_caminantes(n):
    grafico=[]
    for i in range(n):
        grafico.append(randomwalk(N))
    return grafico
   

#%%

def maximos():
    
   '''Arma una lista con el valor extremo de cada 'caminante'
   precondicion: grafico = lista de numpy array]
   poscondicion: Devuelve una lista con el valor mas extremos de cada array del grafico
   '''
   lista_maximos = []
   for i in grafico:
       maxi= i.max()
       mini= i.min()
       extremos=[]
       if abs(maxi) > abs(mini):
           extremos.append(abs(maxi))
       else:
           extremos.append(abs(mini))
       lista_maximos.append(extremos)
        
   return lista_maximos


  
  
#%%
 
def extremos(a):
    extremo=[]
    if a == 'maximo':
        extremo = max(maximos())
    if a == 'minimo':
        extremo = min(maximos())
    return extremo
 


#%%

def buscar_posicion(a): 
    lista = maximos()
    e = extremos(a)
    pos = -1    
    for i,z in enumerate(lista):
        if z == e:
            pos = i
    return pos        
 
#%%
grafico = grafico_caminantes(12)

fig = plt.figure()
plt.subplot(2, 1, 1)
for i in grafico:
    plt.plot(i)
    

max_extremos = extremos('maximo') 
posicion = buscar_posicion('maximo')
min_extremos = extremos('minimo')
posicion_min = buscar_posicion('minimo')
       


#%%

plt.xlabel("Tiempo")
plt.ylabel("Distancia al origen")
plt.title("Caminatas al azar")
plt.xlim(0,N + 3000)
plt.ylim(-1000,1000)
plt.legend()


plt.subplot(2, 2, 3)

plt.plot(grafico[posicion])
plt.xlabel("Tiempo")
plt.ylabel("Distancia al origen")
plt.xlim(0, 100000)
plt.ylim(-900,900)

#plt.title("Caminatas al azar")

plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4)
plt.plot(grafico[posicion_min])   
plt.xlabel("Tiempo")
plt.ylabel("Distancia al origen")
plt.xlim(0, 100000)
plt.ylim(-900,900)
#plt.title("Caminatas al azar")

plt.xticks([]), plt.yticks([])



plt.show()

