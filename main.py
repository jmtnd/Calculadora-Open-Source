from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

while True:
    print("\nCalculadora Open Source")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Suma avanzada")
    print("6. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "6":
        print("¡Hasta luego!")
        break

    if opcion in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: Ingrese números válidos.")
            continue

        if opcion == "1":
            resultado = sumar(num1, num2)
        elif opcion == "2":
            resultado = restar(num1, num2)
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
        elif opcion == "4":
            resultado = dividir(num1, num2)

        print(f"Resultado: {resultado}")

    elif opcion == "5":
        try:
            n = int(input("¿Cuántos números desea sumar? "))
            if n < 1:
                print("Debe ingresar al menos un número.")
                continue
            numeros = []
            for i in range(n):
                num = float(input(f"Ingrese el número {i+1}: "))
                numeros.append(num)
            resultado = suma_avanzada(*numeros)
            print(f"Resultado: {resultado}")
        except ValueError:
            print("Error: Ingrese un número válido.")
    else:
        print("Opción no válida. Intente de nuevo.")