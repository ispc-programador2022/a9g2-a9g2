# pryecto A9G2
2
#Importamos la función bienvenida
#Importamos la función ing2i
#Importamos la función ing2s

from funciones.presentacion import presentacion
from funciones.ing2i import ing2i
from funciones.ing2s import ing2s

presentacion()

enteros = ing2i()
print('Los enteros ingresados son: ', enteros[0], enteros[1])

cadenas = ing2s()
print('Los strings ingresados son: ', cadenas[0], cadenas[1])

