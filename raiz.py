import math 

def raiz(numero):
    r=str(math.sqrt(numero))
    entero = True
    decimal = False


    for i in r:
        print(i)
        if(decimal==True):
            if i== "0":
                entero = True
                
            elif i !="0":
                entero = False 
                print("El numero no tiene raiz entera")

    if (entero == True):
        print("El numero tiene raiz entera")

numero = int(input("Ingrese un numero:"))
raiz(numero)
