try:
    n = int(input("Ingrese un número entero positivo: "))

    if n < 0:
        print("Error: Debe ingresar un número mayor o igual a 0.")
    else:
        pares = list(range(0, n + 1, 2))
        for fila in range(0, len(pares), 10):
            for i in pares[fila : fila + 10]:
                print(str(i), end=" ")
            print()

except ValueError:
    print("Error: Entrada no válida. Por favor, ingrese solo números enteros.")