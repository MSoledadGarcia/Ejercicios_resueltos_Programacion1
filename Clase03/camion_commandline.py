
import csv
import sys

def costo_camion(nombre_archivo):
         with open (nombre_archivo, "rt") as f:
             
            #f = open(nombre_archivo, "rt", encoding= "utf8")
            rows = csv.reader(f)
            headers = next(rows)
            total_fruta= 0
            costo_total= 0
            for row in rows:
                try: 
                    total_fruta= int(row[1])*float(row[2])
                    round(total_fruta, 2)
                    costo_total += total_fruta
                    
                except ValueError:
                    print("Faltan datos")
         return costo_total
        

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = "../Data/camion.csv"
    
costo = costo_camion(nombre_archivo)
print(costo)
