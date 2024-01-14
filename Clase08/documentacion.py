# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:42:33 2022

@author: maria
"""

def valor_absoluto(n):
    '''
    Al pasar como parametro
    cualquier numero entero, devuelve 
    su valor abosluto. 
    pre= n = numero entero
    pos= n = valor absoluto
    inv= n
    '''
    if n >= 0:
        return n
    else:
        return -n #devuelve valor absoluto porque cambia el signo del numero negativo
    
    
#valor = valor_absoluto(8)
#print(valor)    

#%%
def suma_pares(l):
    '''Suma solo los valores pares de una lista
    pre: Lista de numeros enteros
    pos: res: sumatoria de los valores pares de la lista
    inv:res
    '''
    
    res = 0
    for e in l:
        print(f'res= {res}, e = {e}')
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res


#l= [1,4,5,-6,7,8,9]
#suma = suma_pares(l)
#print(suma)
#%%
def veces(a, b):
    '''
    Suma a , b cantidad de veces
    pre: ingresar en a un numero 
    entero y en b un numero >=0
    pos: res = a*b
    inv: res
    '''
    res = 0
    nb = b
    while nb != 0: 
        #print(nb * a + res)
        res += a
        nb -= 1
    return res


#result= veces(6,-3)
#print(result)

#%%
def collatz(n):
    '''
    
    pre: n > 0
    pos: res = cantidad de ciclos hasta llegar a n=1
    inv: res
    '''
    res = 1

    while n!=1: #si n es negativo nunca se interrumpe el ciclo
        if n % 2 == 0:
            n = n//2
            print(f'res={res}, n={n} ')
        else:
            n = 3 * n + 1 
        res += 1
        print(f'res={res}, n={n} ')
    return res

#funcion = collatz(11)
#print(funcion)
