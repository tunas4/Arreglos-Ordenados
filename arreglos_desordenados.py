class ArreglosDesordenados:
    def __init__(self, tamano):
        self.max = tamano
        self.a = [None] * tamano
        self.n = -1

    def mostrar(self):
        if self.n == -1:
            print("Arreglo vacío")
        else:
            for i in range(self.n):
             print(self.a[i])

    def insertar(self, valor):
        if self.n < self.max:
            self.a[self.n] = valor
            self.n += 1
        else:
            print("Arreglo Lleno")

    def buscar(self, valor):
        for i in range(self.n):
            if valor == self.a[i]:
                return i 
        return -1
    def eliminar(self, valor):
        resp = self.buscar(valor)
        if resp != -1:
            for i in range(resp,self.n -1):
                self.a[i] = self.a[self.a+1]
            self.a[self.n - 1] = None
            self.n -= 1
            return resp
        return -1

    def modificar(self, valor):
        resp = self.buscar(valor)
        if resp > -1:
            nuevo_valor = input("Escribe el nuevo valor:")
            self.a[resp] = nuevo_valor
            return resp
        return -1


        

        






    
