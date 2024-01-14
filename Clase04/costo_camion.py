#Ejercicio 4.3: Un ejemplo práctico de enumerate()
#Ejercicio 4.4: La función zip()

import csv
def costo_camion(nombre_archivo):
         with open (nombre_archivo, 'rt') as f:
             
            filas = csv.reader(f)
            encabezados = next(filas)
            costo_total = 0
            for nfila, fila in enumerate(filas, start = 1):
                record = dict(zip(encabezados,fila))
                try: 
                    ncajones = int(record['cajones'])
                    precio = float(record['precio'])
                    costo_total += ncajones * precio
                    
                except ValueError:
                    print(f'Fila {nfila} puede interpretar: {fila}')
         return costo_total
        
                    
               
        
 

costo = costo_camion('../Data/fecha_camion.csv')
print(costo )