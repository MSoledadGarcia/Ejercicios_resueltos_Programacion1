

archivo = r'C:\Users\maria\Downloads\Ejercicios\ejercicios_python\Data\camion.csv'
f= open(archivo, "rt", encoding= "utf8")
headers = next(f).split(",")
total_fruta= 0
costo_total= 0
for line in f:
    fila = line.split(",")
    total_fruta= int(fila[1])*float(fila[2])
    round(total_fruta, 2)

    costo_total += total_fruta
print(costo_total)




f.close()  
    
    



