

#Ejercicio 4.12: Tablas de multiplicar
#No respete la consiga de usar solo suma porque no me salio la manera de hacerlo... sigo intentando. 

print('%6d %3d %3d %3d %3d %3d %3d %3d %3d %3d' % (0,1,2,3,4,5,6,7,8,9))

guion = "-"
print(f'{guion:->43s}')
for i in range(10):
    
    print(f'{i}:{i*0:>4d}{i*1:>4d}{i*2:>4d}{i*3:>4d}{i*4:>4d}{i*5:>4d}{i*6:>4d}{i*7:>4d}{i*8:>4d}{i*9:>4d}')    
