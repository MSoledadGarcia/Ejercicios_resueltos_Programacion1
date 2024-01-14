# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:41:51 2022

@author: maria
"""
#Ejercicio 7.14: Complejidad de incrementar()

def incrementar(s):
    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s


s = [0, 0, 0, 0, 0]
incrementar(s)

n = len(s)
#%%
#Ejercicio 7.15: Un ejemplo más complejo

def listar_secuencias(n):
    lista = [0]*n
    print(lista)
    cont=1
    while 0 in lista:
        secuencia = incrementar(lista)
        print(secuencia)
        cont +=1
    return cont
    
listar_secuencias(4)



#%%
#Ejemplo de clase:
for i in range(n):
    print(i, end=' ')
    for j in range(n):
        print(j,end=' ')
        print(i+j)     #Complejidad de algoritmos n^2. es exponencial
        
        
