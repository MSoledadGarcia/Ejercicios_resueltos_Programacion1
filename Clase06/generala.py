

import random
#from collections import Counter

#Ejercicio 6.1: Generala servida

def tirar(n):
    tirada = []
    for i in range(n):
        tirada.append(random.randint(1,6))
    return tirada
    
def es_generala(tirada):
    if max(tirada) == min(tirada):
        return True
    else:
        return False
#%%
    
N = 100000
G = sum([es_generala(tirar(5)) for i in range(N)])
G
prob = G/N*100
prob
#promedio = 1000000//745
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
print(f'Podemos estimar que sale una generala servida cada {promedio} tiradas')


#%%


#Ejercicio 6.2: Generala no necesariamente servida

def cant_repetidas(tirada,n):
    cantidades = n*[0]
    cantidades
    #tirada= tirar(5)

    for i in tirada:
        cantidades[i-1] +=1
    maximo = max(cantidades)  
    numero = cantidades.index(maximo) + 1
    lista_repes = maximo * [numero]
    return  lista_repes

#tirada = tirar(5)
#n = 6
#repes = cant_repetidas(tirada, n)
#print(repes)

#%%


def generala(): 
    jugadas = []
    n = 5
    tiradas = 1
    if tiradas == 1:
        tirada = tirar(5)
        #print(tirada)
        if es_generala(tirada):
            return True
        else:
            repes = cant_repetidas(tirada, 6)
            for i in repes:
                jugadas.append(i)
            tiradas += 1
    if tiradas == 2:
        n = len(tirada) - len(repes) 
        tirada_2 = tirar(n) 
        #print(tirada_2)
        for i in tirada_2:
            if i in jugadas:
                jugadas.append(i)
    tiradas += 1
    if tiradas == 3:
        n = len(tirada) - len(jugadas) 
        tirada_3 = tirar(n)
        #print(tirada_3)
        for i in tirada_3:
            if i in jugadas:
                jugadas.append(i)
    if len(jugadas) == 5:
       return True
    else:
        return False

def prob_generala(N):
    G = sum([generala() for i in range(N)])
    prob = 100*G/N
    promedio = N // G
    
    print(f'Jugue {N} veces, de las cuales {G} saqué generala.')
    print(f'La probabilidad de obtener generala en hasta 3 tiros es de {prob}%')
    #print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')
    print(f'Podemos estimar que sale una generala cada {promedio} jugadas de hasta 3 tiros')

    return prob, promedio

prob_generala_no_servida = prob_generala(100000)
#print(prob_generala_no_servida)





#%%

 
 
 
 