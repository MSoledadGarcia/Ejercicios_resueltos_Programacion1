# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 10:12:40 2022

@author: maria
"""

import matplotlib.pyplot as plt
import numpy as np

temperaturas = np.load('../Data/temperaturas.npy')
plt.hist(temperaturas,bins=10)
plt.title("Mediciones de Temperatura, distribución normal")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Frecuencia")
plt.show
