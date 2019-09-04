from tkinter import *
from tkinter import ttk

raiz=Tk()
raiz.geometry('600x600')
raiz.configure(bg = 'beige')
raiz.title('Aplicación')
ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)
raiz.mainloop()