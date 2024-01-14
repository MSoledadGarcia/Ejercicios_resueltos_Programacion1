
#%%

#Ejercicio 3.6:Propagación:
#(con ayuda del video de la Unidad 6)

def propagar(lis):
    for i,f in enumerate(lis):
       if i-1 >= 0:#para q no de vuelta la lista, q no vaya el -1
           if f == 0 and lis[i-1] == 1:
               lis[i] = 1
               
    for i in range(len(lis)-1, -1, -1):      #(ultimo elemento, para atras, restando de 1 en 1)    
       if i + 1 < len(lis):#puede simplificarse
           if lis[i] == 0 and lis[i+1] == 1:
               lis[i] = 1
               
    return lis

    
lista_1 = [0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
lista_2 = [ 0, 0, 0, 1, 0, 0]

propagar(lista_1)
propagar(lista_2)


#%%
def propagar(lis):
    for i, f in enumerate(lis):
        if f == 0 and lis[i -1] == 1:# si no pongo un limite el [0] cambia el [-1]