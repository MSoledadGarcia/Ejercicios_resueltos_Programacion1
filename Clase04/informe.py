

import csv

def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        #fila = next(filas)
        for fila in filas:
            record = dict(zip(encabezados,fila))
        
            camion.append(record)
        return camion 
    


def leer_precios(nombre_archivo):
    f = open(nombre_archivo, "r")
    rows = csv.reader(f)
    precios = {}
    for row in rows:
        try:
            precios[row[0]]=float(row[1])

        except IndexError: 
            pass
    f.close()
    return precios
    

archivo_camion= "../Data/fecha_camion.csv"
archivo_precios = "../Data/precios.csv"

camion = leer_camion(archivo_camion)
venta = leer_precios(archivo_precios)





def balance (archivo_precios, archivo_camion):
    gasto = 0.0
    ganancia = 0.0
  
    for d in camion:
        gasto += int(d["cajones"])* float(d["precio"])
        ganancia += venta[d["nombre"]]*int(d["cajones"])
    diferencia = ganancia - gasto
       
    return print(round(diferencia, 2))
   
         
        
balance(archivo_precios, archivo_camion)


camion= leer_camion("../Data/camion.csv")
from collections import Counter
tenencias = Counter()
for s in camion:
    tenencias[s["nombre"]]+= int(s["cajones"])
    
print(tenencias)

    
camion= leer_camion("../Data/camion2.csv")
from collections import Counter
tenencias2 = Counter()
for s in camion:
    tenencias2[s["nombre"]]+= int(s["cajones"])
    
print(tenencias2) 

combinadas = tenencias + tenencias
print(combinadas)


#%%
#Ejercicio 5.8: Reduccion de secuencias

camion= leer_camion("../Data/camion.csv")
costo = sum([int(s['cajones'])* float(s['precio']) for s in camion ])
costo

precios= leer_precios("../Data/precios.csv")
valor = sum([int(s['cajones'])* float(precios[s['nombre']]) for s in camion ])
valor

#%%
#Ejercicio 5.9: Consultas de datos

mas100 = [s for s in camion if int(s["cajones"]) > 100]
mas100

myn = [s for s in camion if s ["nombre"] in {"Mandarina", "Naranja"}]
myn

costo10k = [s for s in camion if int(s["cajones"])*float(s["precio"]) > 10000]
costo10k

#%%
#Ejercicio 5.10: Extracción de datos

nombre_cajones = [(s["nombre"], s["cajones"]) for s in camion]
nombre_cajones #LISTA DE TUPLAS

nombres =  {s["nombre"] for s in camion}
nombres #{ } CONJUNTO DE NOMBRES

stock = {nombre:0 for nombre in nombres}
stock #ESPECIFICANDO CLAVE:VALOR

for s in camion:
    stock[s["nombre"]] += int(s["cajones"])

stock #DICCIONARIO DE PRECIOS DE VENTAS

camion_precios = {nombre:precios[nombre] for nombre in nombres}
camion_precios




