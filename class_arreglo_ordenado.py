class ArregloOrdenado:
    def __init__(self):
        self.MAX = 20
        self.arregloOrdenado = [''] * self.MAX
        self.N = -1

    def mostrar(self):
        if self.N == -1:
            return "El arreglo está vacío."
        return self.arregloOrdenado[:self.N+1]

    def definirArreglo(self):
        self.N = -1
        print("Arreglo reiniciado.")

    def busquedaLineal(self, valor: str):
        encontrado = False
        for i in range(self.N + 1):
            if self.arregloOrdenado[i] == valor:
                print(f"Valor '{valor}' encontrado en {i}.")
                print(f"Intentos: {i+1}")
                encontrado = True
                break

        if not encontrado:
            print(f"No se ha encontrado el valor '{valor}' en {i} intentos.")

    def busquedaLinealEliminar(self, valor: str):
        for i in range(self.N + 1):
            if self.arregloOrdenado[i] == valor:
                return i
        return -1

    def busquedaBinaria(self, valor: str):
        li, ls, intentos, encontrado = 0, self.N, 1, False
        while li <= ls:
            medio = (li + ls) // 2
            if self.arregloOrdenado[medio] == valor:
                print(f"Valor '{valor}' encontrado en {medio}.")
                print(f"Intentos: {intentos}")
                encontrado = True
                break
            elif self.arregloOrdenado[medio] < valor:
                li = medio + 1
            else:
                ls = medio - 1
            intentos += 1

        if not encontrado:
            print(f"No se ha encontrado el valor '{valor}' en {intentos} intentos.")

    def insertar(self, valor: str):
        if self.N >= self.MAX - 1:
            print("No se puede insertar, el arreglo está lleno.")
            return

        i = 0
        while i <= self.N and (self.arregloOrdenado[i].lower() < valor.lower() or (self.arregloOrdenado[i].lower() == valor.lower() and self.arregloOrdenado[i] < valor)):
            i += 1

        for j in range(self.N, i - 1, -1):
            self.arregloOrdenado[j + 1] = self.arregloOrdenado[j]

        self.arregloOrdenado[i] = valor
        self.N += 1
        print(f"Valor '{valor}' insertado correctamente.")

    def eliminar(self, valor: str):
        index = self.busquedaLinealEliminar(valor)
        if index != -1:
            for i in range(index, self.N):
                self.arregloOrdenado[i] = self.arregloOrdenado[i + 1]
            self.N -= 1
            print(f"Valor '{valor}' eliminado correctamente.")
        else:
            print("El valor no se encontró.")

    def modificar(self, valor: str):
        index = self.eliminar(valor)
        if index != -1:
            nuevo_valor = input("Introduce el nuevo valor: ")
            self.insertar(nuevo_valor)
        else:
            print("No se puede modificar, valor no encontrado.")

    def todoElArreglo(self):
        print(self.arregloOrdenado)

