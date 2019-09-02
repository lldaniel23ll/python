'''hacer un programa que simule un cajero con un saldo inicial de 1000
y tendra el siguiente menu de opciones
1-ingresar dinero a la cuenta
2-retirar dinero de la cuenta
3- mostrar dinero disponible
4-salir'''

saldo=1000
usuario=float(input("Digite 1 para ingresar dinero a la cuenta\n 2 para retirar dinero de la cuenta\n"
            "3 para mostrar dinero disponible\n4 para salir\n"))
if (usuario==1):
    cuenta=float(input("Cuanto dinero desa ingresar? "))
    saldo+=cuenta
    input(f"Su saldo es de {saldo:.2f}")
elif (usuario==2):
    cuenta=float(input("Cuanto dinero desa retirar"))
    saldo-=cuenta
    input(f"Su saldo es de {saldo:.2f}")
elif (usuario==3):
    input("Su saldo es de",saldo)
elif (usuario==4):
    input("Escogio salir del programa")
else:
    print("ERROR")
