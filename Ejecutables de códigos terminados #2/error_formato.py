while True:
    try:
        numero = int(input("Ingrese un numero entero: "))
        print("Numero ingresado:", numero)
        break  # Sale del ciclo si el número es válido
    except ValueError:
        print("Error: Debe ingresar un numero valido. Intente de nuevo.")