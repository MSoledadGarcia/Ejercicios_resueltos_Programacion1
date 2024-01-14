
#Ejercicio 4.13: Lectura de los árboles de un parque

#(FALTA AGREGAR TIPO DE OBJETO)

from pprint import pprint
import csv
archivo = '../Data/arbolado-en-espacios-verdes.csv'

def leer_parque(archivo, parque):
    with open(archivo, 'rt', encoding = 'utf8') as f:
        arboles = []
        rows = csv.reader(f)
        headers = next(rows)
    
        for row in rows:
            arbol = dict(zip(headers, row))
            
            
            
            if arbol['espacio_ve'] == parque:
                arboles.append(arbol)
                
    return arboles
           
parque= leer_parque(archivo, "GENERAL PAZ")
pprint(len(parque))




#%%
#Ejercicio 4.14: Determinar las especies en un parque

def especies(lista_arboles):
    lista_especies = []
    for arbol in lista_arboles:
        especie = arbol['nombre_com']
        lista_especies.append(especie)
    return set(lista_especies)

conjunto_especies = especies(parque)
#print(conjunto_especies)
        
#%%
#Ejercicio 4.15: Contar ejemplares por especie
from collections import Counter

def contar_ejemplares(lista_arboles):
    lista_ejemplares = []
    for arbol in lista_arboles:
         ejemplar= arbol["nombre_com"]
         lista_ejemplares.append(ejemplar)
         cantidad_ejemplares = Counter(lista_ejemplares)
    return cantidad_ejemplares
    
cantidad = contar_ejemplares(parque)
#pprint(cantidad)

#%%      
        
parque_gral_paz = leer_parque(archivo,'GENERAL PAZ')
ejemplares_gral_paz= contar_ejemplares(parque_gral_paz)
#print(ejemplares_gral_paz.most_common(5))

parque_los_andes = leer_parque(archivo,'ANDES, LOS')
ejemplares_los_andes= contar_ejemplares(parque_los_andes)
#print(ejemplares_los_andes.most_common(5))

parque_centenario = leer_parque(archivo,'CENTENARIO')
ejemplares_parque_centenario= contar_ejemplares(parque_centenario)
#print(ejemplares_parque_centenario.most_common(5))




#%%

#Ejercic'io 4.16: Alturas de una' especie en una lista

def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        if arbol["nombre_com"] == especie:
            altura = float(arbol["altura_tot"])
            alturas.append(altura)
    return alturas
    
altura_especie = obtener_alturas(parque_gral_paz, "Jacarand�")
print(f'Altura maxima de la especie en Parque Gral. Paz: {max(altura_especie)}')
prom =sum(altura_especie)/ len(altura_especie)
print(f'Altura promedio de la especie {prom:.2f}')
print()
altura_especie = obtener_alturas(parque_los_andes, "Jacarand�")
print(f'Altura máxima de la especie en Parque Los Andes: {max(altura_especie)}')
prom = sum(altura_especie)/ len(altura_especie)
print(f'Altura promedio de la especie: {prom:.2f}')
print()
altura_especie = obtener_alturas(parque_centenario, "Jacarand�")
print(f'Altura máxima de la especie en Parque Centenario: {max(altura_especie)}')
prom = sum(altura_especie)/ len(altura_especie)
print(f'Altura promedio de la especie:{prom:.2f}')


#%%
#Ejercicio 4.17: Inclinaciones por especie de una lista

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol["nombre_com"] == especie:
            inclinacion = float(arbol["inclinacio"])
            inclinaciones.append(inclinacion)
    return inclinaciones
    
    
inclinacion_esp_centenario = obtener_inclinaciones(parque_centenario,"Jacarandá")

    
inclinacion_esp_los_andes =obtener_inclinaciones(parque_los_andes,"Jacarandá")

obtener_inclinaciones(parque_gral_paz,"Jacarandá")
    
    
print(f'Inclinaciones en Parque Centenario:{inclinacion_esp_centenario}') 
    
#%%
#Ejercicio 4.18: Especie con el ejemplar más inclinado
#(Con ayuda de un compañero)

def especimen_mas_inclinado(lista_arboles):
    inclinaciones={}
    maximo = 0.0
    especimen = ""
    for i in especies(lista_arboles):
        inclinacion = obtener_inclinaciones(lista_arboles,i)
        inclinaciones[i] = inclinacion
    
    for x,z in inclinaciones.items():
        if maximo < max(z):
            especimen = x
            maximo = max(z)
    return especimen,maximo

 
arbol_mas_inclinado = especimen_mas_inclinado(parque_centenario)
print(f'El arbol más inclinado del Parque Centenario es: {arbol_mas_inclinado}')

    
#%%
#Ejercicio 4.19: Especie más inclinada en promedio

#Lo envio cuando lo termine... 
def especie_promedio_mas_inclinada(lista_arboles):
    inclinaciones = []
    for especie in especies(lista_arboles):
        inclinacion = obtener_inclinaciones(lista_arboles, especie)
        inclinaciones.append(inclinacion)
        
    promedios = []
    for i in inclinaciones:  
        promedio = sum(i)/len(i)
        promedios.append(promedio)
        maximo_promedio = max(promedios)
        
    return maximo_promedio   
        

promedios = especie_promedio_mas_inclinada(parque_los_andes)
print(promedios)

    
    
    
    
    
    
    