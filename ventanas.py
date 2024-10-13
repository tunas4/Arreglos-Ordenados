import tkinter as tk
from class_arreglo_ordenado import ArregloOrdenado

ArregloOrdenado = ArregloOrdenado()

class Views:
    def __init__(self):
        pass

    def ventana_inicializar_arreglo(self):
        ventana_inicializar = tk.Toplevel()
        ventana_inicializar.title("Inicializar / Borrar Arreglo")
        ventana_inicializar.geometry("250x100")

        def validar_valor():
            res = ArregloOrdenado.definirArreglo()
            label_resultado.config(text=res)

        button1 = tk.Button(ventana_inicializar, text="Inicializar / Borrar Arreglo", command=validar_valor)
        button1.pack(pady=10)

        label_resultado = tk.Label(ventana_inicializar, text="")
        label_resultado.pack(pady=10)

    def ventana_mostrar_arreglo(self):
        ventana_mostrar = tk.Toplevel()
        ventana_mostrar.title("Mostrar Arreglo")
        ventana_mostrar.geometry("500x100")

        array = ArregloOrdenado.mostrar()
        label = tk.Label(ventana_mostrar, text=array)
        label.pack(pady=10)

    def ventana_busqueda_lineal(self):
        ventana_busqueda_lineal = tk.Toplevel()
        ventana_busqueda_lineal.title("Búsqueda Lineal")
        ventana_busqueda_lineal.geometry("200x200")

        entry = tk.Entry(ventana_busqueda_lineal)
        entry.pack(pady=10)

        def validar_valor():
            letra = entry.get()
            if len(letra) == 1 and letra.isalpha():
                res = ArregloOrdenado.busquedaLineal(letra)
                label_resultado.config(text=res)
            else:
                label_resultado.config(text="Debes ingresar solo una letra.")

        button6 = tk.Button(ventana_busqueda_lineal, text="Buscar", command=validar_valor)
        button6.pack(pady=10)

        label_resultado = tk.Label(ventana_busqueda_lineal, text="")
        label_resultado.pack(pady=10)

    def ventana_busqueda_binaria(self):
        ventana_busqueda_binaria = tk.Toplevel()
        ventana_busqueda_binaria.title("Búsqueda Binaria")
        ventana_busqueda_binaria.geometry("200x200")

        entry = tk.Entry(ventana_busqueda_binaria)
        entry.pack(pady=10)

        def validar_valor():
            letra = entry.get()
            if len(letra) == 1 and letra.isalpha():
                res = ArregloOrdenado.busquedaBinaria(letra)
                label_resultado.config(text=res)
            else:
                label_resultado.config(text="Debes ingresar solo una letra.")

        button6 = tk.Button(ventana_busqueda_binaria, text="Buscar", command=validar_valor)
        button6.pack(pady=10)

        label_resultado = tk.Label(ventana_busqueda_binaria, text="")
        label_resultado.pack(pady=10)

    def ventana_buscar_arreglo(self):
        ventana_buscar = tk.Toplevel()
        ventana_buscar.title("Buscar Arreglo")
        ventana_buscar.geometry("200x200")

        button3 = tk.Button(ventana_buscar, text="Búsqueda Lineal", command=self.ventana_busqueda_lineal)
        button3.pack(pady=10)

        button4 = tk.Button(ventana_buscar, text="Búsqueda Binaria", command=self.ventana_busqueda_binaria)
        button4.pack(pady=10)

    def ventana_insertar_arreglo(self):
        ventana_insertar = tk.Toplevel()
        ventana_insertar.title("Insertar Arreglo")
        ventana_insertar.geometry("200x200")

        label = tk.Label(ventana_insertar, text="Introduce el valor:")
        label.pack(pady=10)

        entry = tk.Entry(ventana_insertar)
        entry.pack(pady=10)

        def validar_valor():
            letra = entry.get()
            if len(letra) == 1 and letra.isalpha():
                res = ArregloOrdenado.insertar(letra)
                label_resultado.config(text=res)
            else:
                label_resultado.config(text="Debes ingresar solo una letra.")

        boton_validar = tk.Button(ventana_insertar, text="Insertar", command=validar_valor)
        boton_validar.pack(pady=10)

        label_resultado = tk.Label(ventana_insertar, text="")
        label_resultado.pack(pady=10)

    def ventana_eliminar_arreglo(self):
        ventana_eliminar = tk.Toplevel()
        ventana_eliminar.title("Eliminar Arreglo")
        ventana_eliminar.geometry("200x200")

        label = tk.Label(ventana_eliminar, text="Introduce el valor:")
        label.pack(pady=10)

        entry = tk.Entry(ventana_eliminar)
        entry.pack(pady=10)

        def validar_valor():
            letra = entry.get()
            if len(letra) == 1 and letra.isalpha():
                res = ArregloOrdenado.eliminar(letra)
                label_resultado.config(text=res)
            else:
                label_resultado.config(text="Debes enviar solo una letra.")

        button6 = tk.Button(ventana_eliminar, text="Borrar", command=validar_valor)
        button6.pack(pady=10)

        label_resultado = tk.Label(ventana_eliminar, text="")
        label_resultado.pack(pady=10)

    def ventana_modificar_arreglo(self):
        ventana_modificar = tk.Toplevel()
        ventana_modificar.title("Modificar Arreglo")
        ventana_modificar.geometry("200x250")

        label = tk.Label(ventana_modificar, text="Valor a modificar:")
        label.pack(pady=10)

        entry = tk.Entry(ventana_modificar)
        entry.pack(pady=10)

        label2 = tk.Label(ventana_modificar, text="Nuevo valor:")
        label2.pack(pady=10)

        entry2 = tk.Entry(ventana_modificar)
        entry2.pack(pady=10)

        def validar_valor():
            letra = entry.get()
            letra2 = entry2.get()
            if len(letra) == 1 and letra.isalpha():
                res = ArregloOrdenado.modificar(letra, letra2)
                label_resultado.config(text=res)
            else:
                label_resultado.config(text="Debes enviar solo una letra.")

        button6 = tk.Button(ventana_modificar, text="Modificar", command=validar_valor)
        button6.pack(pady=10)

        label_resultado = tk.Label(ventana_modificar, text="")
        label_resultado.pack(pady=10)

    def ventana_creditos(self):
        ventana_creditos = tk.Toplevel()
        ventana_creditos.title("Créditos")
        ventana_creditos.geometry("200x200")

        label1 = tk.Label(ventana_creditos, text="Creado por: Tu Nombre Aquí")
        label1.pack(pady=20)
