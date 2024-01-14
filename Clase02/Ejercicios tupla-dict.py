import csv
f = open(r"C:\Users\maria\Downloads\Ejercicios\ejercicios_python\Data\camion.csv")
filas = csv.reader(f)
headers = next(filas)
fila = next(filas)
#print(fila)

t = (fila[0], int(fila[1]), float(fila[2]))
#print(t)

cost = t[1]*t[2]
#print(f"{cost:0.2f}")

t= (t[0], 75, t[2])


nombre, cajones, precio = t
t = (nombre, 3*cajones, precio)
#print(t)


#Ejercicio 2.11: Diccionarios como estructuras de datos
d = {
    "nombre": fila[0],
    "cajones": int(fila[1]),
    "precio": float(fila[2])
}
#print(d)

cost = d["cajones"]* d["precio"]
#print(cost)

d["cajones"] = 75
cost = d["cajones"]* d["precio"]
#print(cost)

d["fecha"]= (14,8,2020)
d["cuenta"]= 12345
#print(d)

#Ejercicio 2.12: Más operaciones con diccionarios
"""for k in d:
    #print("k: ", k)
    print(f"{k}= {d[k]}")

items = d.items()
print(items)
for k,v in d.items():
    print(k,"=", v)

#print(list(d))
claves= d.keys()
print(claves)"""

nuevos_items = [('nombre', 'Manzanas'), ('cajones', 100), ('precio', 490.1), ('fecha', (13, 8, 2020))]

d = dict(nuevos_items)
print(d)

f.close()  
