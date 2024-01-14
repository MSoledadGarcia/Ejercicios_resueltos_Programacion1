# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:57:33 2022

@author: maria
"""
import datetime

#Ejercicio 10.2: Cuánto falta

def cuanto_falta():
    primavera = datetime.date(2023, 9, 21)
    hoy = datetime.date.today()
    falta = primavera - hoy
    
    return print(f' faltan {falta} para que llegue la primavera')


primavera= cuanto_falta()
#%%
#Ejercicio 10.3: Fecha de reincorporación

inicio_licencia = datetime.date(2020, 9, 26)
dias = datetime.timedelta(days = 200)
fin_licencia = inicio_licencia + dias
print(fin_licencia)

#%%

