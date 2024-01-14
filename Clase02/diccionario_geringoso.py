

def dict_geringoso (palabra):
    
    cadena = ""
    capadepenapa = ""
     
    for c in palabra:
        capadepenapa += c 
        if c in  "aeiou":
            capadepenapa +="p"+c
            
    return capadepenapa



lista =["Banana", "Manzana", "Mandarina"]
lista2=[]
for palabra in lista:
    lista2.append(dict_geringoso(palabra))

diccionario = dict(zip(lista,lista2))
print(diccionario)




def pasar_a_dicc(lista):

    lista2=[]
    for palabra in lista:
        lista2.append(dict_geringoso(palabra))
    
    diccionario = dict(zip(lista,lista2))
    return diccionario


print(pasar_a_dicc(['rosa', 'azul', 'violeta']))