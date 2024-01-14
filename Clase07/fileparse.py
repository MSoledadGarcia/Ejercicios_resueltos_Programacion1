# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 10:47:14 2022

@author: maria
"""

# fileparse.py
import csv

def parse_csv(nombre_archivo, select = None, types= False, has_headers= True):
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
            for row in rows:
                if not row:    # Saltea filas sin datos
                    continue
                
                if indices: # Filtrar la fila si se especificaron columnas
                    row = [row[index] for index in indices]
                
                if types:
                        row = [func(val) for func, val in zip(types, row)]
                    #registro = {name:func(val) for name, func, val in zip(headers, types, row)}  
                    
                registro = dict(zip(headers, row))
                registros.append(registro) 
                    
    
            return registros
    
        if has_headers == False:
            lista_precios = []
            for row in rows:
                if not row:
                    continue
                if types:
                    
                    row = [func(val) for func, val in zip(types, row)]
                    
                    
                lista_precios.append(tuple(row))        
                 
        return lista_precios
    
#Lee todos los datos
#camion = parse_csv('../Data/camion.csv', types=[str,int,float])
#camion
#precios = parse_csv('../Data/precios.csv',  types=[str,float], has_headers = False)
#precios
#%%
#lee solo algunos datos

#cajones_retenidos = parse_csv('../Data/camion.csv', select = ['nombre', 'cajones'], types = [str, int], has_headers = True)
#cajones_retenidos

