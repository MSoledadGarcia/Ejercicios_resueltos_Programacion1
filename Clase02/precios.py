archivo= r'C:\Users\maria\Downloads\Ejercicios\ejercicios_python\Data\precios.csv'


f = open (archivo, "rt", encoding= "utf8")
"""fruta = (input("Ingrese nombre de fruta:")) 
for line in f:
    fila = line.split(",")
    if fruta in fila:
        print("El precio de ", fruta, "es: " , fila[1])

f.close()"""

for line in f:
    fila = line.split(",")
    if "Naranja" in fila:
        print("El precio de la naranja es: ", fila[1])

f.close()