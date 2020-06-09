import os 
numero = 201343871
lista1= []
lista2=[]
valor1=0
Valor2=0
while numero != 1:
    if numero % 2 == 0:
        print("%d," % (numero), "\n")
        numero = numero / 2
        valor1= str(numero)
        file=open("collatz.txt","a" )
        file.write(valor1)
        file.write("\n ")
        file.close
        

    else:
        print("%d," % (numero), "\n")
        numero = (numero * 3) + 1
        Valor2=str (numero)
        file=open("collatz.txt","a" )
        file.write(Valor2)
        file.write("\n")
        file.close
    if numero == 1:
        print("1")