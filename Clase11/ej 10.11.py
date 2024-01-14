# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 14:29:43 2022

@author: maria
"""

#Ejercicio 11.10: Ejemplo de getattr()

import lote
c = lote.Lote('Peras', 100, 490.1)
columnas = ['nombre', 'cajones']
for colname in columnas:
    print(colname, '=', getattr(c, colname))