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
        return ("Arreglo inicializado / borrado exitosamente.")

    def busquedaLineal(self, valor: str):
        for i in range(self.N + 1):
            if self.arregloOrdenado[i] == valor:
                return (f"Valor '{valor}' encontrado en {i}. \nIntentos: {i+1}")
        
        return (f"No se encontro el valor '{valor}' \nIntentos: {i+1}")

    def busquedaLinealCambio(self, valor: str):
        for i in range(self.N + 1):
            if self.arregloOrdenado[i] == valor:
                return i
        return -1

    def busquedaBinaria(self, valor: str):
        li, ls= 0, self.N
        intentos = 0

        # Si el valor esta en limite inferior o superior del arreglo se retorna.
        if self.arregloOrdenado[li] == valor:
            return (f"Valor '{valor}' encontrado en {li}. \nIntentos: {intentos}")
            
        elif self.arregloOrdenado[ls] == valor:
            return (f"Valor '{valor}' encontrado en {ls}. \nIntentos: {intentos}")
    
        # Busqueda binaria
        while li <= ls:
            P = (li + ls) // 2 # Calculamos el punto medio.

            if self.arregloOrdenado[P] == valor:
                return (f"Valor '{valor}' encontrado en {P}. \nIntentos: {intentos}")
            
            elif (self.arregloOrdenado[P].lower() < valor.lower() or (self.arregloOrdenado[P].lower() == valor.lower() and self.arregloOrdenado[P] < valor)):
                    li = P + 1
            else:
                    ls = P - 1

            intentos += 1  # Incrementamos el contador de intentos.

        return(f"No se ha encontrado el valor '{valor}' en {intentos} intentos.")

    def insertar(self, valor: str):
        if self.N >= self.MAX - 1:
            return "Arreglo lleno."

        i = 0
        while i <= self.N and (self.arregloOrdenado[i].lower() < valor.lower() or (self.arregloOrdenado[i].lower() == valor.lower() and self.arregloOrdenado[i] < valor)):
            i += 1

        for j in range(self.N, i - 1, -1):
            self.arregloOrdenado[j + 1] = self.arregloOrdenado[j]

        self.arregloOrdenado[i] = valor
        self.N += 1
        return "Valor insertado correctamente."

    def eliminar(self, valor: str):
        index = self.busquedaLinealCambio(valor)
        if index != -1:
            for i in range(index, self.N):
                self.arregloOrdenado[i] = self.arregloOrdenado[i + 1]
            self.N -= 1
            return (f"Valor '{valor}' eliminado correctamente.")
        else:
            return ("El valor no se encontró.")

    def modificar(self, valor: str, valorModificado: str):
        index = self.eliminar(valor)
        if index != -1:
            self.insertar(valorModificado)
            return (f"Valor '{valor}' modificado correctamente.")
        else:
            return ("El valor no se encontró.")

    def todoElArreglo(self):
        print(self.arregloOrdenado)

