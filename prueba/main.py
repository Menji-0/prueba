# ------ NO BORRAR -----
from funciones import *
from herramientas import *
# ------ NO BORRAR -----


#menu principal
while (True):
    alergias = []
    print("Bienvenido usuario!")
    nombre = input("Ingrese su nombre: ")
    com_fav = input("Ingrese su comida favorita: ")
    alergia = input("Tiene alguna alergia alimenticia? (s/n): ")
    while alergia == "s":
        alergia_a_ingresar = input("Ingrese su alergia (si tiene mas de una primero ingrese una): ").lower()
        alergias.append(alergia_a_ingresar)
        preguntar = input("Tiene alguna otra alergia? (s/n): ")
        if (preguntar == "n"):
            break
        else:
            alergia = "s"
    
    user = {'nombre':nombre,
            'com_fav':com_fav,
            'alergias':alergias
            }
    menu = []
    
    menu_general()
