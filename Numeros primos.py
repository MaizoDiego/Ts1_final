a = int(input("Ingresar un número: "))


def primo(numero):
    if numero < 2:
        return False
    elif numero == 2:
        return True
    else:
        for i in range (2, numero):
            if numero % i == 0:
                return False
        return True
        
print("¿El número escogido es primo:?", primo(a))