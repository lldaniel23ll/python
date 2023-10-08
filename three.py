def imprimir_arbol(altura):
    for i in range(1, altura + 1):
        print(" " * (altura - i) + "*" * (2 * i - 1))

altura = int(input("Ingrese la altura del árbol: "))
imprimir_arbol(altura)

