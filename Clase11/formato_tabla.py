# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 13:32:37 2022

@author: maria
"""

# formato_tabla.py

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()
        




class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()
        
        
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))   
        
        
class FormatoTablaHTML(FormatoTabla):
    def encabezado(self, headers):
        print('<tr>', end= '')
    
        for h in headers:
            print(f'<th>{h}</th>', end ='')            
        print('</tr>')
        
        
    def fila(self, data_fila):
        print('<tr>', end= '')
        for d in data_fila:
            print(f'<td>{d}</td>', end ='')
        print('</tr>')
       
   
        
def crear_formateador(fmt):
    
    if fmt == 'txt':
        formateador = FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = FormatoTablaCSV()
    elif fmt == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    return formateador
           
            
        