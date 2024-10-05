from class_arreglo_ordenado import ArregloOrdenado

def main():
    arreglo = ArregloOrdenado()

    while True:
        print("\nOpciones:")
        print("1. Inicializar/Borrar arreglo")
        print("2. Mostrar arreglo")
        print("3. Buscar")
        print("4. Insertar")
        print("5. Eliminar")
        print("6. Modificar")
        print("7. Créditos")
        print("8. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            arreglo.definirArreglo()

        elif opcion == '2':
            print(arreglo.mostrar())

        elif opcion == '3':
            valor = input("Introduce el valor a buscar: ")
            if len(valor) != 1 or not valor.isalpha():
                print("Error: Debes ingresar solo una letra.")
            else:
                print("1. Búsqueda lineal")
                print("2. Búsqueda binaria")
                tipo_busqueda = input("Elige el tipo de búsqueda: ")

                if tipo_busqueda == '1':
                    print(arreglo.busquedaLineal(valor))
                elif tipo_busqueda == '2':
                    print(arreglo.busquedaBinaria(valor))
                else:
                    print("Tipo de búsqueda no válido.")

        elif opcion == '4':
            valor = input("Introduce el valor a insertar: ")
            if len(valor) != 1 or not valor.isalpha():
                print("Error: Debes ingresar solo una letra.")
            else:
                arreglo.insertar(valor)

        elif opcion == '5':
            valor = input("Introduce el valor a eliminar: ")
            if len(valor) != 1 or not valor.isalpha():
                print("Error: Debes ingresar solo una letra.")
            else:
                arreglo.eliminar(valor)

        elif opcion == '6':
            valor = input("Introduce el valor a modificar: ")
            if len(valor) != 1 or not valor.isalpha():
                print("Error: Debes ingresar solo una letra.")
            else:
                arreglo.modificar(valor)

        elif opcion == '7':
            print("Créditos: Programa creado por [Tu Nombre]")

        elif opcion == '8':
            print("Saliendo del programa...")
            break

        elif opcion == '9':
            arreglo.todoElArreglo()

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
