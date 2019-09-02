#pedir que el usuario digite un caracter y vocal y que la maquina indique si es una vocal o no
letra= input("Digite un caracter: ").upper()

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print(f"{letra} es una vocal")
else:
    print(f"{letra} es una consonante")