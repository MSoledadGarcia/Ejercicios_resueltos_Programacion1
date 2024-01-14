# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 00:04:18 2022

@author: maria
"""
import random

def tirar(n):
    tirada = []
    for i in range(n):
        tirada.append(random.randint(1,6))
    return tirada
    

tirada = (tirar(5))
print(tirada)


def es_generala(tirada):
    if max(tirada) == min(tirada):
        return True
    else:
        return False
    
    

 
def cant_repetidas(tirada,n):
    cantidades = n*[0]
    #tirada= tirar(5)

    for i in tirada:
        cantidades[i-1] +=1
    maximo = max(cantidades)  
    numero = cantidades.index(maximo) + 1
    lista_repes = maximo * [numero]
    return  lista_repes

repes =cant_repetidas(tirada,6)
print(repes)




def tirar_de_nuevo():    
    n = len(tirada) - len(repes) 
    nueva_tirada = tirar(n)
    '''for i in nueva_tirada:
        if i in repes:
            repes.append(i)'''
    return nueva_tirada
         
nueva_tirada= (tirar_de_nuevo())
print(nueva_tirada)


jugadas = []
n = 5
tiradas = 1
if tiradas == 1:
    tirada = tirar(5)
    if es_generala(tirada):
        print("Generala servida!")
    else:
        repes = cant_repetidas(tirada, 6)
        jugadas.append(repes)
        tiradas += 1
if tiradas == 2:
    tirada_2 = tirar_de_nuevo() 
    for i in tirada_2:
        if i in jugadas:
            jugadas.append(i)
            print(jugadas)
      




if es_generala(tirada):
    print("Generala servida!")
    #break
else:
    repes = cant_repetidas(tirada, 6)
    jugadas.append(repes)
    #jugadas += repes
tirada_2 = tirar_de_nuevo()
for i in tirada_2:
    if i in jugadas:
        jugadas.append(tirada_2[i])
tirada_3 = tirar_de_nuevo()
for i in tirada_3:
    if i in jugadas:
        jugadas.append(i)

   
return jugadas
    
''' #if len(jugadas) == 5: 
    #    print("Generala")
        #break
    #else:
    repes2 = cant_repetidas(tirada, 6)
        #jugadas += repes
    jugadas.append(repes2)
    tirada_3 = tirar_de_nuevo()
    if len(jugadas) == 5:
        print("Generala")
        #break
    else:
        repes = cant_repetidas(tirada, 6)
        #jugadas += repes
        jugadas.append(repes)
        
return jugadas'''
        
tiro_dados = mano()
tiro_dados
    