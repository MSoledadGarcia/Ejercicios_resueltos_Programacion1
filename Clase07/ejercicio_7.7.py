# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:14:05 2022

@author: maria
"""

#Ejercicio 7.7: Importar módulos

import os
os.getcwd()



import informe_funciones
import fileparse
help(fileparse)
dir(fileparse)

camion = fileparse.parse_csv('../Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
camion
lista_precios = fileparse.parse_csv('../Data/precios.csv', types = [str, float], has_headers = False)
lista_precios

precios = dict(lista_precios)
precios
precios['Naranja']

#%%
from fileparse import parse_csv
camion = parse_csv('../Data/camion.csv', select = ['nombre','cajones', 'precio'], types = [str,int,float])
camion
