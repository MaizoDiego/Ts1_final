def capicua (num):
    x=str(num)
    lista=list(x)
    if lista==lista[::-1]:
        return True

a = int(input("Ingrese: "))
if capicua (a) == True:
    print("Es un número capicua")
else:
    print("No es un número capicua")