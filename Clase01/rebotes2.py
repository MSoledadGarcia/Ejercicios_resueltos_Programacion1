# rebotes.py
# Archivo de ejemplo
# Ejercicio

import sys
if len(sys.argv) == 2:
    altura = int(sys.argv[1])
else:
    altura = 100

rebote = altura/ 5 *3


cantidad_rebotes = 1

while cantidad_rebotes <=10:
    print (cantidad_rebotes, round(rebote, ndigits=2))
    rebote = (rebote /5)*3
    
    cantidad_rebotes= cantidad_rebotes + 1