# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 10:30:02 2022

@author: maria
"""
#Ejercicio 11.1: Objetos como estructura de datos.

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = int(cajones)
        self.precio = float(precio)
        
    def costo(self):
        costo =self.cajones * self.precio
        return costo
    
    def vender(self, vendidos):
        self.cajones -= vendidos
       
    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
     

    
a = Lote('Pera', 100, 490.10)    
repr(a)



import informe_final
camion = informe_final.leer_camion('../Data/camion.csv')
camion
#%%
'''
a = Lote('Pera', 100, 490.10)
b = Lote('Manzana', 50, 122.34)
c = Lote('Naranja', 75, 91.75)

c.cajones*c.precio

lotes = [a, b, c]
lotes

for c in lotes:
     print(f'{c.nombre:>10s} {c.cajones:>10d} {c.precio:>10.2f}')
'''

