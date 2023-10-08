from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('600x600')
root.configure(bg='beige')
root.title('Aplicación')

# Crear el frame principal
frame_principal = Frame(root)
frame_principal.pack(pady=50)

# Crear el frame secundario dentro del frame principal
frame_secundario = Frame(frame_principal)
frame_secundario.pack()

# Crear la barra de progreso dentro del frame secundario
pb = ttk.Progressbar(frame_secundario, orient="horizontal", length=200, mode="determinate")
pb.pack(pady=20)
pb.start()

# Botón de salida
ttk.Button(root, text='Salir', command=quit).pack(side=BOTTOM)

root.mainloop()
