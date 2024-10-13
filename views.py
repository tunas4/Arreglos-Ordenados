import tkinter as tk
from ventanas import Views

def main():
    views = Views()

    ventana = tk.Tk()
    ventana.title("Arreglos")
    ventana.geometry("250x375")

    button1 = tk.Button(ventana, text="Inicializar / Borrar Arreglo", command=views.ventana_inicializar_arreglo)
    button1.pack(pady=10)

    button2 = tk.Button(ventana, text="Mostrar Arreglo", command=views.ventana_mostrar_arreglo)
    button2.pack(pady=10)

    button3 = tk.Button(ventana, text="Buscar", command=views.ventana_buscar_arreglo)
    button3.pack(pady=10)

    button4 = tk.Button(ventana, text="Insertar", command=views.ventana_insertar_arreglo)
    button4.pack(pady=10)

    button5 = tk.Button(ventana, text="Eliminar", command=views.ventana_eliminar_arreglo)
    button5.pack(pady=10)

    button6 = tk.Button(ventana, text="Modificar", command=views.ventana_modificar_arreglo)
    button6.pack(pady=10)

    button7 = tk.Button(ventana, text="Créditos", command=views.ventana_creditos)
    button7.pack(pady=10)

    button8 = tk.Button(ventana, text="Salir", command=ventana.destroy)
    button8.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()
