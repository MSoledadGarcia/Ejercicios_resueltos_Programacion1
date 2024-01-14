
import csv
def costo_camion (nombre_archivo):
    
    f= open(nombre_archivo, "rt", encoding= "utf8")
    headers = next(f).split(",")
    total_fruta= 0
    costo_total= 0
    for line in f:
        fila = line.split(",")
        total_fruta= int(fila[1])*float(fila[2])
        round(total_fruta, 2)

        costo_total += total_fruta
    return costo_total

costo = costo_camion("..\Data\camion.csv")
print(costo)

"""
import csv
def costo_camion(nombre_archivo):
    total = 0.0

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows):
            try:
                ncajones = int(row[1])
                precio = float(row[2])
                total += ncajones * precio
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return print(total)


archivo = '../Data/camion.csv'

costo_camion(archivo)"""