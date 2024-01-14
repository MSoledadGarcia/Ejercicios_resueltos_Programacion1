#Ejercicio 1.18: Geringoso rústico

def geringoso(palabra):
    
    cadena= palabra
    capadepenapa=""
    
    for c in cadena:
        capadepenapa += c
        if c in "aeiou":
            capadepenapa += "p"+c
    return capadepenapa

geringoso("probando")
    #%%    
