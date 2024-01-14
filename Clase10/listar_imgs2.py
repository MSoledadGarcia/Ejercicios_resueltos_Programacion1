# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 18:15:31 2022

@author: maria
"""
import os
'''
def archivos_png(directorio):
    #os.chdir(directorio)
    for root, dirs, files in os.walk("."):
        for name in files:
            if '.png ' in name:
                print(os.path.join(root, name))
        for name in dirs:
            if '.png ' in name:
                print(os.path.join(root, name))
 '''     
 #%%
def archivos_png(directorio):
    #os.chdir(directorio)
    lista = [n for n in os.walk(directorio) if '.png' in n]   
    return lista

 
lista_png = archivos_png('../Data/ordenar')
print(lista_png)
        
#%%
        

def archivos_png(directorio):
    for root, dirs, files in os.walk(directorio):
       for name in files:
           if '.png' in name:
               print(os.path.join(root, name))
       for name in dirs:
           if '.png' in name:
               print(os.path.join(root, name))


              
lista_png = archivos_png('../Data/ordenar')
print(lista_png)
        
#%%


def archivos_png2(directorio):
    for root, dirs, files in os.walk(directorio):
        print(files)
       
        for name in files:
           
           if '.png' in name:
               print(name)
       for name in dirs:
           if '.png' in name:
               print(name)

lista_png2 = archivos_png2('../Data/ordenar')
print(lista_png2)


#%%
def archivos_png3(directorio):
    lista= [name for root, dirs, files in os.walk(directorio) for name in files  if '.png' in name ]
    return lista



lista_png3 = archivos_png3('../Data/ordenar')
print(lista_png3)

#%%
for root, dirs, files in os.walk('../Data/ordenar'):
    for file in files:
        print(file)
    
    for name in files:
        if '.png' in name:
            print(name)
    for name in dirs:
        if '.png' in name:
            print(name)


#%%
[file for root, dirs, files in os.walk('../Data/ordenar')for file in files if file.endswith(".png")]

#%%
[file if file.endswith(".png") for file in files for root, dirs, files in os.walk('../Data/ordenar')]














