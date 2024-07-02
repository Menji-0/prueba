"""
Puede escribir aqui las funciones del codigo
Se importaran de forma automatica al 'main.py'
"""
# ------ NO BORRAR -----
def test () -> None:
    """
        Funcion para probar el archivo
    """
    import herramientas
    menu = herramientas.load_items('menu.csv')
    print(menu)

# esto es para que test solo corra si es ejecutado directamente
if __name__ == '__main__':
    test()
# ------ NO BORRAR -----

#Escribir Funciones desde aqui hacia abajo ------------

#ejemplo de funcion
def menu_general () -> any:
    import herramientas
    comida_selec = []
    print("Seleccione la accion que quiera realizar")
    print("1. ver menu","\n""2. ver carrito")
    selec = int(input("Su seleccion: "))
    if (selec == 1):
        test()
        while selec == 1:
            prod_sel = input("Seleccione una comida (escriba el nombre tal y como se muestra en el menu): ")
            if (prod_sel in herramientas.load_items('menu.csv')):
                comida_selec.append(prod_sel)
            s = int(input("Quiere seleccionar otro alimento? (1 = si/ 2 = no): "))
            if (s == 1):
                continue
            if (s == 2):
                break
    print(comida_selec)



