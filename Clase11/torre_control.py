# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:20:13 2022

@author: maria
"""


    
class TorreDeControl:
    
    def __init__(self):
        '''Crea una lista vacia '''
        self.items = []
        self.items_con_prioridad = []
    
    def nuevo_arribo(self, x):
        '''Agrega al avion a la lista para asignar 
        pista CON prioridad'''
        self.items_con_prioridad.append(x)
        
    def nueva_partida(self, x):
        '''Agrega al avion a la lista para asignar 
        pista SIN prioridad'''
        self.items.append(x)
        
    def ver_estado(self):
        if self.esta_vacia():
           print('No hay vuelos en espera.')
        else:
           
           print(f'Vuelos esperando para aterrizar: {", ".join(self.items_con_prioridad)} \nVuelos esperando para despegar: {", ".join(self.items)}')
    
    def asignar_pista(self):
        if self.esta_vacia():
            print('No hay vuelos en espera.')
            
        else:    
            if len(self.items_con_prioridad):
                res = self.items_con_prioridad.pop(0)
                print( f'El vuelo {res} aterrizó con exito.')
                
            else:
                res = self.items.pop(0)
                print( f'El vuelo {res} despegó con exito.')
           
    def largo_lista(self):
        '''Devuelve el largo de la lista.'''
        largo = len(self.items) + len(self.items_con_prioridad)
        return largo
    
    def esta_vacia(self):
        '''Devuelve 
        True si la lista esta vacia, 
        False si no.'''
        return self.largo_lista() == 0
    
        
        #%%
        
        
torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()      
torre.asignar_pista()      
torre.asignar_pista()      
        
        
        
        