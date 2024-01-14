# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:16:29 2022

@author: maria
"""

import pandas as pd
import os

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)

type(df)
type(df['long'])

df.columns

df.id_arbol

df.index
#se puede cambiar los indices y tomar una columna como indice, por ej id_arbol

df.loc[1]


cols = ['altura_tot', 'diametro', 'inclinacio']
df.loc[513:520, cols]

df.loc[513:520[1,2,3]]

df['lat'] #--> serie  
df[['lat']] #--> columna 

#%%
#series de tiempo
pd.date_range('20200923', periods = 7)


pd.date_range('20200923 14:00', periods = 7)


pd.date_range('20200923 14:00', periods = 6, freq = 'H')


#not so sure. guide to latex

#%%
cantidad_ejemplares=df['nombre_com'].value_counts()
cantidad_ejemplares
#%%

df_jacarandas = df[df['nombre_com'] == 'Jacarandá']
cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df_jacarandas[cols]
df_jacarandas.describe()

df_jacarandas.plot.scatter(x = 'diametro', y = 'altura_tot')

#%%
cantidad_ejemplares.index

df.loc[165] #indice
cantidad_ejemplares.loc['Eucalipto']

df_jacarandas.iloc[0] #numero de posicion


#%%
#Caminatas al azar

import numpy as np

idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index= idx)
s2 = s1.cumsum()
s2

s2.plot()
#%%
w = 5
s3 = s2.rolling(w).mean()
s3.plot()

#%%

horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']

df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
df_walks.plot()
#%%
w= 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() #datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav #cambio el nombre de las columnas
                             #para los datos suavizados
                             
df_walk_suav.plot()

