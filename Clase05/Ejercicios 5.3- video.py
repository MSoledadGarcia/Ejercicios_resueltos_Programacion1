# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
lista = [1, 3, 5, 7]

if 20 in lista:
    pos = lista.index(20)
else:
     pos = -1

print(pos)
  
  #%%
def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
         
    for i, z, in enumerate (lista):  # recorremos los elementos de la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
        i += 1       
    return pos

busqueda_lineal([1, 4, 54, 3, 0, -1], 44)


#%%
#otro manera de hacer lo mismo con while

def buscar_elem(lista,e):
    i =0
    pos = -1
    while i < len(lista):
        if lista[i] == e:
            pos = i
            break  #--> lo uso si quiero que me muestre el primer valor. 
        i += 1
        
    return pos

l = [3,6,7,1,9,-2]
l2 = [3,6,-2,7,1,9,-2,-3]

buscar_elem(l2,-2)

##########################################


def buscar_elem2(lista,e):
    p = len(lista) -1
    
    while (p >= 0) and (lista[p] != e):
        p -= 1
        
    return p

buscar_elem2(l2, 44)
buscar_elem2(l2,-2)    
    
 ############################################   
def buscar_elem3(lista,e):
    pos = -1
    for i in range(len(lista)):
        if lista[i] == e:
            pos = i
            break
    return pos 

buscar_elem3(l2,-2)    

############################################
def buscar_elem4(lista,e):
    pos = -1
    for idx, elem in enumerate(lista):
        if elem == e:
            pos = idx
            #break
        
    return pos


buscar_elem4(l2,-2)    
    
        
        
        
        
        
        

        