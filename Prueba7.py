#pedir tres numeros y decir cual es el msyor
num1=int(input("Digite un numero "))
num2=int(input("Digite un numero "))
num3=int(input("Digite un numero "))

if num1>num2 and num1>num3:
    print(f"{num1} es mayor ")
if num2>num1 and num2>num3:
    print(f"{num2} es msyor")
if num3>num1 and num3>num2:
    print(f"{num3} es mayor")
elif num1==num2 and num1==num3:
    print("Los tres son iguales")
