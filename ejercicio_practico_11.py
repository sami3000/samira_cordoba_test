from modulo_ejercicio_11 import suma, resta, division, multiplicacion


menu= """  menu
        1- suma
        2- resta
        3- division
        4- multiplicacion 
        5- par e impar
        6- acumulador
        """

print (menu)

opcion= int(input("ingrese una opcion: "))


if opcion == 1: 
    suma()

elif opcion == 2: 
    resta()

elif opcion == 3: 
    division()

elif opcion == 4: 
    multiplicacion()
    
# elif opcion==5:
#     pares_impares()
    
# elif opcion== 6:
#     acumulador()
    




