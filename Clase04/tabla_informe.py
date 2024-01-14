

import csv

def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
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
    

archivo_camion= "../Data/camion.csv"
archivo_precios = "../Data/precios.csv"





def balance (archivo_precios, archivo_camion):
    
    camion = leer_camion(archivo_camion)
    venta = leer_precios(archivo_precios)

    gasto = 0.0
    ganancia = 0.0
  
    for d in camion:
        gasto += int(d["cajones"])* float(d["precio"])
        ganancia += venta[d["nombre"]]*int(d["cajones"])
    diferencia = ganancia - gasto
       
    return print(round(diferencia, 2))
   
         
        
balance(archivo_precios, archivo_camion)



#Ejercicio 4.8: Recolectar datos
#Ejercicio 4.9: Imprimir una tabla con formato
#Ejercicio 4.10: Agregar encabezados
#Ejercicio 4.11: Un desafío de formato


headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    
    
def hacer_informe(archivo_a, archivo_b):
    
    lista_ = []
    for d in archivo_a:
        recolectar = d["nombre"], int(d["cajones"]), float(d["precio"]) , (float(archivo_b[d["nombre"]]) - float(d["precio"]))
        
        lista_.append(recolectar)
       
    return lista_

camion = leer_camion(archivo_camion)
venta = leer_precios(archivo_precios)

informe = hacer_informe(camion, venta)

guion = "-"
print(f'{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}')
print('-'*10, '-'*10, '-'*10, '-'*10)
#for r in informe:
   
      #  print('%10s %10d %10.2f %10.2f' % r)
for nombre, cajones, precio, cambio in informe:
    peso="$"
    print(f'{nombre:>10s} {cajones:>10d} {peso:>4s}{precio:>6.2f} {cambio:>10.2f}')
        
        