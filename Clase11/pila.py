# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:00:34 2022

@author: maria
"""

class Pila():
    
    def __init__(self):
        self.items = []
     
    
    def apilar(self, diccionario):
        self.items.append(diccionario)
        
        
        
    def desapilar(self):
        self.items.pop()
        
        
    def esta_vacia(self):
      
        if len(self.items) == 0:
            print('la pila está vacia')
        else:
            print('la pila no esta vacia')
        
        
        
   
#%%

def mostrar_x_del_estado(estado):
    print(f"Ejecutando {estado['función']}(), x vale {estado['variables']['x']}")  
       
#%%

pila_de_llamadas = Pila()
print(pila_de_llamadas)
#la ejecución está en la línea 3 de g(). El estado tiene x=10.
estado = {'función': 'g', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 10, 'b': 45}}

mostrar_x_del_estado(estado)
#sigo ejecutando, toca llamar a f(): incremento y apilo el estado.
estado['próxima_línea_a_ejecutar'] = 5

pila_de_llamadas.apilar(estado)

#llamo a f y ejecuto primeras líneas
estado = {'función': 'f', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 50, 'a': 20}}

mostrar_x_del_estado(estado)

#termina ejecución de f: se desapila el estado:
estado = pila_de_llamadas.desapilar()
mostrar_x_del_estado(estado)          
