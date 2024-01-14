archivo = r'C:\Users\maria\Downloads\Ejercicios\ejercicios_python\Data\camion.csv'
"""with open (archivo, 'rt', encoding ='utf8') as f:
    data = f.read()

data
print(data)"""

with open (archivo, 'rt', encoding ='utf8') as f:
    for line in f:
        print(line, end ="")