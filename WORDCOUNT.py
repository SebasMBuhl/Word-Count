import tkinter as tk
import string

root = tk.Tk()
root.geometry("400x400")
root.title("Word Count")

tk.Label(root, text="¿Qué palabra quieres buscar?").pack(pady=5)
palabra = tk.Text(root, height=2, width=20)
palabra.pack(pady=5)

tk.Label(root, text="Introduce el texto en el que se buscara la palabra:").pack(pady=5)
busqueda= tk.Text(root, height=10, width=30)
busqueda.pack(pady=10)

resultado = tk.Label(root, text="", wraplength=400, justify="center")
resultado.pack(pady=20)



def count():
    txt_palabra = palabra.get("1.0", tk.END).strip()
    txt_busqueda = busqueda.get("1.0", tk.END).strip()

    txt_busqueda= txt_busqueda.lower()
    txt_palabra= txt_palabra.lower()

    translator = str.maketrans("", "", string.punctuation)
    txt_busqueda = txt_busqueda.translate(translator)

    num = txt_busqueda.split().count(txt_palabra)

    resultado.config(text=f"La palabra '{txt_palabra}' aparece {num} veces")

boton = tk.Button(root, text="Buscar", command=count)
boton.pack(pady=10)


root.mainloop()
