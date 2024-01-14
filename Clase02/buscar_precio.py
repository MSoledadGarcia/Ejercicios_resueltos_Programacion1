def buscar_precio(fruta):

    archivo = '../Data/precios.csv'

    f = open (archivo, "rt", encoding= "utf8")
    si_esta= False
    for line in f:
        fila = line.split(",")
        if fruta in fila:
            si_esta = True
            break
    if si_esta:

        print("El precio del cajon de", fruta, "es:" , float(fila[1]))
        
    else:
        print(fruta, "no figura en el listado de precios")

    f.close()

buscar_precio("Frambuesa")
buscar_precio("Kale")