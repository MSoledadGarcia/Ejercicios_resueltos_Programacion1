import gzip
archivo = r'C:\Users\maria\Downloads\Ejercicios\ejercicios_python\Data\camion.csv.gz'

with gzip.open(archivo , "rt", encoding= "utf8") as f:
    for line in f:
        print(line, end=" ")


