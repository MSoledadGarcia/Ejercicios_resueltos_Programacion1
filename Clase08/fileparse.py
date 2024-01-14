# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 22:07:17 2022

@author: maria
"""


import csv

 
def parse_csv(lineas, select = None, types= False, has_headers= True, silence_errors = False):
    
    '''
    Parsea un objeto iterable en una lista de registros.
    El parámetro select permite elegir algunas columnas en caso de que no se requieran ver todas, 
    types: permite pasar una lista con el tipo de objeto de cada columna
    has_headers: se refiere a si tiene o no encabezados y para usar el parametro select debe ser True
    silence_errors: atrapa los errores de tipo ValueError que puedan aparecer en el texto. 
    '''
        
    rows = csv.reader(lineas)  
    if has_headers:
        
    
        headers = next(rows)
      
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
        registros = []
        for i, row in enumerate(rows, start = 1):
            #print (row)
            if select:
                indices = [headers.index(nombre_columna) for nombre_columna in select]
                headers = select
            else:
                indices = []
                
                
            if not row:    # Saltea filas sin datos
                continue
            
                
            if indices: # Filtrar la fila si se especificaron columnas
                row = [row[index] for index in indices]
            try:
                if types:
                        row = [func(val) for func, val in zip(types, row)]
                    #registro = {name:func(val) for name, func, val in zip(headers, types, row)}  
                    
                registro = dict(zip(headers, row))
                registros.append(registro) 
                
            except ValueError as e:
                if silence_errors == False:
                    print(f'Fila {i}: No puede convertir {row}')
                    print(f'Fila {i}: Motivo: {e}')
        return registros

    if has_headers== False:
        lista_precios = []
        for i, row in enumerate(rows, start=1):
            if not row:
                continue
            try:
                if types:
                    
                    row = [func(val) for func, val in zip(types, row)]
                    
                
                lista_precios.append(tuple(row)) 
            except ValueError as e:
                if silence_errors == False:
                    print(f'Fila {i}: No puede convertir {row}')
                    print(f'Fila {i}: Motivo: {e}')
        
        if select:
            raise RuntimeError ("Para seleccionar, necesito encabezados.")
             
        return lista_precios
   #%%
   
#with open('../Data/camion.csv', 'rt') as f:
 #   #rows = csv.reader(f)
  #  camion = parse_csv(f, select = ['nombre','precio'],types= [str, int, float], has_headers = False)

#print(camion)

lines = ['nombre,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
camion = parse_csv(lines, types=[str,int,float], has_headers=True)
camion

