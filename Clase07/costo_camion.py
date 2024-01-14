
'''

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
        '''
                    
               
        #%%
 

import informe_funciones
def costo_camion(archivo):
    camion = informe_funciones.leer_camion(archivo, types = [str, int, float], has_headers=True)
    costo_total = 0
    for fila in camion:
        costo_total += fila['cajones'] * fila['precio']
    return costo_total
     
    
costo = costo_camion('../Data/camion.csv')
print(costo )





