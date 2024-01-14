

# Ejercicio 5.12: Datos de primera clase


import csv
f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
row


row[1]* row[2]

types = [str, int, float]

types[1](row[1])

types[1](row[1])*types[2](row[2])

r = list(zip(types,row))
r
converted = []
for func, val in zip(types,row):
    converted.append(func(val))
    
converted
converted[1]*converted[2]

dict(zip(headers,converted))

#LO MISMO CON COMPRENSION DE LINEAS
{name:func(val) for name, func, val in zip(headers,types,row)}
