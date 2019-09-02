'''hacer un programa que haga las 4 operaciones aritmeticas
basicas,y hacer que el usuario indique cul operacion usar
cuando oprima su inicial'''
n1=int(input("Digite un entero "))
n2=int(input("Digite otro entero "))
print("-----------------------------------------------")
operacion=input("Digite la inicial de la operacion ").lower()
print("-----------------------------------------------")
if(operacion=='s'):
    n3=n1+n2
    print("la respuesta es",n3)
elif(operacion=='r'):
    n3=n1-n2
    print("la respuesta es", n3)
elif(operacion=='m' and operacion=='p'):
    n3=n1*n2
    print("la respuesta es", n3)
elif(operacion=='d'):
    n3=n1/n2
    print("la respuesta es", n3)
else:
    print("ERROR")