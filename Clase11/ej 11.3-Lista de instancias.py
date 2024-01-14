# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 11:20:25 2022

@author: maria
"""
import lote
import fileparse
with open('../Data/camion.csv') as lineas:
    camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    
camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
camion
sum([c.costo() for c in camion])
