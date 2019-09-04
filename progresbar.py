#grafica
 from tkinter import ttk
 from tkinter import *

 root = Tk()

 pb = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
 pb.pack()
 pb.start()

 root.mainloop()

# en consola
from tqdm import tqdm

loop =tqdm(total = 5000,position = 0,leave = True)

for k in range(5000):
    loop.set_description("Loading...".format(k))
    loop.update(1)

loop.close()