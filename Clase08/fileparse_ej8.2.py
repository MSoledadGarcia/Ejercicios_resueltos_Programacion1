# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 10:47:14 2022

@author: maria
"""

# fileparse.py

#Ejercicio 8.1: Lancemos excepciones

import csv

def parse_csv(nombre_archivo, select = None, types= False, has_headers= True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        
        
        if has_headers:

            # Lee los encabezados
            headers = next(rows)
            
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
            
            if select:
                indices = [headers.index(nombre_columna) for nombre_columna in select]
                headers = select
            else:
                indices = []
                
            registros = []
            for i, row in enumerate(rows, start=1):
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
            for row in rows:
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
    
#Lee todos los datos
#camion = parse_csv('../Data/camion.csv', types=[str,int,float])
#camion
#precios = parse_csv('../Data/precios.csv',  select= None, types=[str,float], has_headers = False)
#precios

#%%
#lee solo algunos datos

#cajones_retenidos = parse_csv('../Data/camion.csv', select = ['nombre', 'precio'], types = [str, float], has_headers = True)
#cajones_retenidos

#%%
#camion = parse_csv('../Data/missing.csv', types = [str,int,float], silence_errors = False)
#camion

#!!!!!!!! para que quede igual al ejemplo... uso enumerate?? o hay otra forma???, esta bien hacer la excepcion tb en la parte sin encabezados?


