while True:
    print("\n===== MENÚ DE PRODUCTOS =====")
    print("1. Leche")
    print("2. Pan")
    print("3. Arroz")
    print("4. Huevos")
    print("5. Aceite")
    print("0. Salir")

    opcion = input("Elija un producto (0-5): ")

    if opcion == "1":
        print("Leche: $1.200")
    elif opcion == "2":
        print("Pan: $800")
    elif opcion == "3":
        print("Arroz: $1.500")
    elif opcion == "4":
        print("Huevos: $3.000")
    elif opcion == "5":
        print("Aceite: $2.500")
    elif opcion == "0":
        print("Gracias por su visita. ¡Hasta pronto!")
        break
    else:
        print("Opción no válida, intente de nuevo.")
        continue

    volver = input("¿Desea volver al menú? (s/n): ")
    if volver != "s":
        print("Gracias por su visita. ¡Hasta pronto!")
        break