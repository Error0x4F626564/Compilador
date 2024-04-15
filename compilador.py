from tkinter import*

ventana_principal = Tk()
ventana_principal.title(string="Compilador")
ventana_principal.minsize(width=600, height=400)
ventana_principal.config(padx=35, pady=35)

# Evitar que se cambie el tamaño de la ventana
ventana_principal.resizable(False, False)

# etiqueta
etiqueta1 = Label(text="Area del codigo", font=("Arial", 14))
etiqueta1.grid(column=0, row=0)

# caja de texto
caja_texto = Text(width=60, height=20, font=("Arial", 14))
caja_texto.grid(column=0, row=1, columnspan=2)

# botón
boton1 = Button(text="Generar Tokens", font=("Arial", 14))
boton1.grid(column=0, row=3, pady=(10, 0))  # Agregar un pequeño relleno en la parte superior del botón

ventana_principal.mainloop()

#Diccionarios
#operadores={}
#data_type={}
#identificador={}