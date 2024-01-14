# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 22:42:33 2022

@author: maria
"""

import numpy as np

#Ejercicio 6.7: arange() y linspace()
a = np.arange(1, 20, 2)
a
b = np.linspace(1, 19, 10, dtype=np.int64)
b

#El vector b tiene datos de tipo float.

#Agregar, borrar y ordenar elementos
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(arr)
arr #continua desordenado, el sort solo muestra una copia ordenada.

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [0,0]])
np.concatenate((x, y), axis=1)

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [0,0]])
np.concatenate((x, y), axis=0)


array_ejemplo = np.array([[[0, 1, 2, 3],
                            [4, 5, 6, 7]],

                           [[0, 1, 2, 3],
                            [4, 5, 6, 7]],

                           [[0 ,1 ,2, 3],
                            [4, 5, 6, 7]]])

array_ejemplo.ndim

#%%

a = np.array([1, 2, 3, 4, 5, 6])
#vec_fila = a[np.newaxis, :]
#vec_fila
vec_col = a[:, np.newaxis]
vec_col

#%%
csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

np.savetxt('new_file.csv', csv_arr)

np.loadtxt('new_file.csv')



