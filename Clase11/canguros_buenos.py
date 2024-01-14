# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 23:29:54 2022

@author: maria
"""

class Canguro:
    
    def __init__(self, nombre, lista = None):
        
        self.nombre = nombre
        if lista == None:
            lista = []
        else:
            lista = lista
        self.contenido_marsupio = lista
    


    def meter_en_marsupio(self, objeto):
        self.contenido_marsupio.append(objeto)
        
        
    def __str__(self):
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

       
    
    def __repr__(self):
        return f'{self.nombre}, {"".join(self.contenido_marsupio)}'
    

    

#%%

# canguro_malo.py
"""Este código continene un 
bug importante y dificil de ver
"""

class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido= None):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        
        self.nombre = nombre
        
        if contenido == None:
            lista = []
        else:
            lista = contenido   
        self.contenido_marsupio = lista


    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

        #%%
madre_canguro = Canguro('Madre', ["hoja"])
print(madre_canguro)
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)
print(cangurito)

