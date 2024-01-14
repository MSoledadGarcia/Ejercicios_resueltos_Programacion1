
#import os
#os.getcwd()
import fileparse
import csv
#%%
def leer_camion(nombre_archivo, select = None, types= False, has_headers= True):
    return fileparse.parse_csv(nombre_archivo, select , types, has_headers)


#%%
def leer_precios(nombre_archivo, select = None, types= False, has_headers= True):
    return dict(fileparse.parse_csv(nombre_archivo, select, types, has_headers ))

#%%
def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], lote['precio'], cambio)
        lista.append(t)
    return lista

#%%

def imprimir_informe(informe):
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
   ###Falta el rturn!!! ?? hace falta??
    
 #%%   
#camion = leer_camion('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float], has_headers=True) 
#precios = leer_precios('../Data/precios.csv', types = [str, float], has_headers = False)


def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion, select = ['nombre', 'cajones', 'precio'], types = [str, int, float], has_headers=True) 
    precios = leer_precios(nombre_archivo_precios, types = [str, float], has_headers = False)
    informe = hacer_informe(camion, precios)     
    informe_completo = imprimir_informe(informe) 



#informe = informe_camion('../Data/camion.csv', '../Data/precios.csv')

