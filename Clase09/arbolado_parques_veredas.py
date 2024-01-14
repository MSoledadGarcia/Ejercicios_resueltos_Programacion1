# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 10:15:32 2022

@author: maria
"""


import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df_parques = pd.read_csv(fname)
df_tipas_parques_ = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'].copy()
df_tipas_parques= df_tipas_parques_[['diametro', 'altura_tot']]
df_tipas_parques= df_tipas_parques.rename(columns = {'altura_tot':'altura'})
df_tipas_parques['ambiente'] = 'parque'


archivo2 = 'arbolado-publico-lineal-2017-2018.csv'
fname2 = os.path.join(directorio,archivo2)
df_veredas = pd.read_csv(fname2)
df_tipas_veredas_ = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'].copy()
df_tipas_veredas = df_tipas_veredas_[['diametro_altura_pecho', 'altura_arbol']]

df_tipas_veredas= df_tipas_veredas.rename(columns = {'diametro_altura_pecho': 'diametro', 'altura_arbol':'altura'})
df_tipas_veredas['ambiente']= 'vereda'


df_tipas_parques 
df_tipas_veredas

df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
 #%%
 
df_tipas.boxplot('diametro',by = 'ambiente')
df_tipas.boxplot('altura',by = 'ambiente')

sns.boxplot(data = df_tipas)

