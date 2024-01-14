
#import os
#os.getcwd()
import fileparse
import sys
import lote
import formato_tabla


#%%
def leer_camion(nombre_archivo, select = None, types= False, has_headers= True):
    with open (nombre_archivo) as f:
        camion_dicts = fileparse.parse_csv(f, select , types, has_headers)
        return [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]    


#%%
def leer_precios(nombre_archivo, select = None, types= False, has_headers= True):
    with open (nombre_archivo) as f:
        return dict(fileparse.parse_csv(f, select, types, has_headers ))


#%%
def hacer_informe(archivo_camion, archivo_precios):
    camion = leer_camion(archivo_camion)
    precios = leer_precios('../Data/precios.csv', types = [str, float], has_headers = False)
    lista = []
    for l in camion:
        precio_venta = precios[l.nombre]
        cambio =  precio_venta - l.precio
        t = (l.nombre, l.cajones, l.precio, cambio)
        lista.append(t)
    return lista





#%%
def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    
    '''
    
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)


#formateador = formato_tabla.FormatoTablaTXT()
#inf = imprimir_informe(informe, formateador )


    #%%   
#camion = leer_camion('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float], has_headers=True) 
#precios = leer_precios('../Data/precios.csv', types = [str, float], has_headers = False)


def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    # Leer archivos con datos
    #camion = leer_camion(nombre_archivo_camion)
    #precios = leer_precios(nombre_archivo_precios)

    # Obtener los datos para un informe
    data_informe = hacer_informe(nombre_archivo_camion, nombre_archivo_precios)

       # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)




#camion = leer_camion('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float], has_headers=True) 
#precios = leer_precios('../Data/precios.csv', types = [str, float], has_headers = False)

#informe=informe_camion('../Data/camion.csv','../Data/precios.csv')


#%%
#Ejercicio 8.4: Funcion principal

def f_principal(archivos):
    
    if len(archivos) < 3 or len(archivos) > 4:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios formato')
    
    
    else:
        
        if len(archivos) == 3:
            camion = archivos[1]
            precios = archivos[2]
            
            informe= informe_camion(camion, precios)
            
        if len(archivos) == 4:
            camion = archivos[1]
            precios = archivos[2]
            fmt = archivos[3]
            
            informe= informe_camion(camion, precios, fmt)
            
        return informe
   
    
if __name__ == '__main__':
    f_principal(sys.argv)




#%%

#import informe_final 
#informe_final.f_principal(['informe_final.py', '../Data/camion.csv', '../Data/precios.csv'])








