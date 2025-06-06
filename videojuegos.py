# Registro de videojuegos
import os, msvcrt

videojuegos = []

plataformas = ("PC", "PS5", "Xbox Series X", "Nintendo Switch")

while True:
    os.system('cls')
    print("\n--- MENÚ DE VIDEOJUEGOS ---")
    print("1: Registrar videojuegos")
    print("2: Ver videojuegos")
    print("3: Modificar videojuego")
    print("4: Eliminar videojuego")
    print("5: Salir")

    opcion = input("Seleccione una opción (1-5): ")
    os.system('cls')

    if opcion=="1":
        pass
    elif opcion=="2":
        pass
    elif opcion=="3":
        pass
    elif opcion=="4":
        pass
    elif opcion=="5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción invalida.")
    print("Presione una tecla para continuar.")
    msvcrt.getch()