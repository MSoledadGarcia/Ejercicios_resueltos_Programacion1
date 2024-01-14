
 
import sys
import informe_final

def costo_camion(archivo):
    camion = informe_final.leer_camion(archivo, types = [str, int, float], has_headers=True)
    costo_total = 0
    for fila in camion:
        costo_total += fila.cajones * fila.precio
    return costo_total
     


def f_principal(argv): 
    print(costo_camion(argv[1]))
    

if __name__ == '__main__':
    f_principal(sys.argv)
    
# no devuelve el return si abro el archivo desde la terminal pero si si lo importo...
#por ese motivo agregue el print en la linea 15

#%%
costo_camion('../Data/camion.csv')
