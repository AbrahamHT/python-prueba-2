palabra=str(input("favor ingresar palabra : "))
Letra=str(input("favor ingresar letra : "))
n=len(palabra)
cont=0
for i in palabra:
    if i == Letra:
        cont=cont+1
print(f"las veces que aparese la letra {Letra} en la palabra {palabra} fueron {cont} ")