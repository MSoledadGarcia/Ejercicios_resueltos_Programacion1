
#%%
#Ejercicio 3.5:Semántica

"""El error en este caso  es semántico y estaba ubicado en el "if".
lo corregi cambiando "if expresion[i] =="a"" por "if "a" in expresion", ya que en el primer 
caso continúa con el else (False) en el primer indice que sea diferente a "a" en cambio en el
segundo caso busca la letra "a" en toda la expresion. 
Otra opcion es sacar el "else" como se hizo en el ejercicio 3.6. """
#Codigo corregido:
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        
        if "a" in expresion:
           
            return True
        else:
            return False
        i += 1
        
print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.6: Sintáxis

"""Este ejercicio tiene varios errores de sintaxis. Le faltan los ":" en def, while 
y en el if. Tambien le falta un "=" cuando realiza la comparación y la palabra reservada False 
está mal escrita. El Codigo corregido es el siguiente: """

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.7: Tipos
"""Este código está pensado para objetos de tipo string, por lo que los parámetros ingresados
deben ser cadenas de texto"""
def tiene_uno(expresion):
    n = len(expresion)
    
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno("1984"))

#%%
#Ejercicio 3.8: Alcances
"""A la función le faltaba el "return", el codigo corregido con el ""return"" es el siguiente:"""

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)

print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.9: Pisando memoria
"""En este código el ultimo  diccionario estaba pisando los anteriores. Lo corregí armando 
 el diccionario de la forma correcta.El código corregido es el siguiente:"""
 
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    #registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {
                encabezado[0] : fila[0],
                encabezado[1] : int(fila[1]),
                encabezado[2] : float(fila[2])
                }
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

    