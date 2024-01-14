#%%
import csv
import os
#os.chdir('../Data/precios.csv')
archivo= r'../Data/precios.csv'
#%%
def buscar_precio(fruta, verbose= True):
    precio = None
    with open (archivo, "rt", encoding= "utf8")as arch:
        archivo_csv = csv.reader(arch)
        for linea in archivo_csv:
            if linea:
                if linea[0]== fruta:
                    precio = float(linea[1])
                    break

    if verbose:
        if precio != None:
            print(f"El precio de un cajón de {fruta} es {precio}")
        else:
            print(f"{fruta} no figura en la lista de precios.")
    return precio


buscar_precio("Frambuesa")
buscar_precio("Kale")
