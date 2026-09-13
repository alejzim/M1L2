import random

while True:
    print("\n--- MENÚ DE TAREAS ---")
    print("1. Generar una contraseña")
    print("2. Mostrar un triángulo de asteriscos")
    print("3. Mostrar tu nombre en un marco de asteriscos")
    print("4. Jugar a adivinar el número")
    print("0. Salir")

    opcion = input("Elige una opción: ").strip()

    if opcion == "0":
        print("¡Hasta luego!")
        break

    elif opcion == "1":
        character = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

        while True:
            try:
                longitud = int(input("Introduce la longitud de la contraseña: "))
                if longitud > 0:
                    break
                print("La longitud debe ser mayor que cero.")
            except ValueError:
                print("Introduce un número entero.")

        contrasena = ""
        for i in range(longitud):
            contrasena += random.choice(character)

        print("Tu contraseña es:", contrasena)

    elif opcion == "2":
        for i in range(1, 6):
            print("*" * i)

    elif opcion == "3":
        nombre = input("Ingresa un nombre: ")
        marco = "*" * (len(nombre) + 2)
        print(marco)
        print("*" + nombre + "*")
        print(marco)

    elif opcion == "4":
        numero_secreto = random.randint(1, 20)
        print("¡Adivina el número del 1 al 20! Tienes 5 intentos.")

        for intento in range(1, 6):
            while True:
                try:
                    numero = int(input(f"Intento {intento}: Ingresa un número del 1 al 20: "))
                    if 1 <= numero <= 20:
                        break
                    print("El número debe estar entre 1 y 20.")
                except ValueError:
                    print("Introduce un número entero.")

            if numero == numero_secreto:
                print("¡Acertaste! Adivinaste el número en", intento, "intento(s).")
                break
            elif numero < numero_secreto:
                print("El número secreto es mayor.")
            else:
                print("El número secreto es menor.")
        else:
            print("No quedan más intentos. El número secreto era", numero_secreto)

    else:
        print("Opción inválida. Elige 0, 1, 2, 3 o 4.")
