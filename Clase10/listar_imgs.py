# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 22:56:34 2022

@author: maria
"""

import os
import sys

def archivos_png(directorio):
    lista= [file for root, dirs, files in os.walk('../Data/ordenar')for file in files if file.endswith(".png")] 
    return lista


def f_principal(argv): 
    print(archivos_png(argv[1]))


if __name__ == '__main__':
    f_principal(sys.argv)
    
#lista_png = archivos_png('../Data/ordenar')
#print(lista_png)
