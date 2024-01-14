# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 10:45:34 2022

@author: maria
"""
from datetime import datetime, date, timedelta

def vida_en_segundos(fecha_nac):
    ''' recibe una fecha de nacimiento en formato str y
    devuelve la cantidad de segundos vividos.
    Pre: fecha de nacimiento en formato str 'dd/mm/AAAA'
    Pos: devuelve numero float.
    '''
    fecha_nac = datetime.strptime(fecha_nac, '%d/%m/%Y')
    tiempo_de_vida = datetime.now() - fecha_nac
    segundos = tiempo_de_vida.total_seconds()
    #print('tiempo de vida:',tiempo_de_vida)
    #print('segundos:', segundos)
    return segundos




tiempo_de_vida= vida_en_segundos('09/08/1985')
print(f'El tiempo de vida en segundos es: {tiempo_de_vida:0.2f}')
