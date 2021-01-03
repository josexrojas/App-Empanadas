#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk

precio = 45
precio = float(precio)

def tomarPedido():
	
	cajaSuma.delete(0, tk.END)
	cajaCobrar.delete(0, tk.END)
	a = cajaCarne.get()
	a = int(a)
	b = cajaJyq.get()
	b = int(b)
	c = cajaAtun.get()
	c = int(c)
	d = cajaHumita.get()
	d = int(d)
	suma = a + b + c + d
	cajaSuma.insert(0, suma)
	aCobrar = suma * precio
	cajaCobrar.insert(0, aCobrar)
	
	
ventana = tk.Tk ()
ventana.config(width = 350, height = 300)
ventana.title("CASA DE EMPANADAS - App")

etiqueta = tk.Label(text = "* Gustos >")
etiqueta.place(x=20, y=10)
etiqueta = tk.Label(text = "______________")
etiqueta.place(x=20, y=25)

etiqueta = tk.Label(text = "* Cantidades >")
etiqueta.place(x=105, y=10)
etiqueta = tk.Label(text = "______________")
etiqueta.place(x=105, y=25)

etiqueta = tk.Label(text = "* Precio $45.-")
etiqueta.place(x=200, y=10)
etiqueta = tk.Label(text = "______________")
etiqueta.place(x=200, y=25)

cajaCarne = tk.Entry()
cajaCarne.place(x=120, y=60, width=40, height=25)
etiqueta = tk.Label(text = "* Carne >")
etiqueta.place(x=20, y=60)

cajaJyq = tk.Entry()
cajaJyq.place(x=120, y=100, width=40, height=25)
etiqueta = tk.Label(text = "* J y Q >")
etiqueta.place(x=20, y=100)

cajaAtun = tk.Entry()
cajaAtun.place(x=120, y=140, width=40, height=25)
etiqueta = tk.Label(text = "* Atún >")
etiqueta.place(x=20, y=140)

cajaHumita = tk.Entry()
cajaHumita.place(x=120, y=180, width=40, height=25)
etiqueta = tk.Label(text = "* Humita >")
etiqueta.place(x=20, y=180)

btnHacerPedidos = tk.Button(text = "Cerrar\nPedido", command = tomarPedido)
btnHacerPedidos.place(x=200, y=60, width=75, height=50)

btnSalir = tk.Button(text = "Salir", command = ventana.destroy)
btnSalir.place(x=200, y=220, width=75, height=50)

etiqueta = tk.Label(text = "______________________________")
etiqueta.place(x=20, y=210)

cajaSuma = tk.Entry()
cajaSuma.place(x=120, y=250, width=40, height=25)
etiqueta = tk.Label(text = "* Unidades  >>>")
etiqueta.place(x=20, y=250)

cajaCobrar = tk.Entry()
cajaCobrar.place(x=200, y=165, width=75, height=30)
etiqueta = tk.Label(text = "> TOTAL $ <")
etiqueta.place(x=200, y=140)

ventana.mainloop()
