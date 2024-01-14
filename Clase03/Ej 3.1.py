
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

costo_camion(archivo)
