
N=0
while N<1 or N>6:
    N=int(input("1)kilometros a millas\n2)millas a kilometros\n3)kilogramos a libras\n4)libras a kilogramos\n5)celcius a fahrenheit\n6)farenheit a celcius\n7)salir\ningrese opcion : "))
    if N==1: 
        km=int(input("favor ingresar km a convertir : "))
        mi=km*0.621371
        print(f"el valor  de km a mi es de {mi}")
    elif N==2:
        mi=int(input("favor ingresar mi a convertir : "))
        km=mi*1.60934
        print(f"el valor  de mi a km es de {km}")
    elif N==3:
        kg=int(input("favor ingresar kg a convertir : "))
        lb=kg*2.20462
        print(f"el valor  de kg a lb es de {lb}")

    elif N==4:
        lb=int(input("favor ingresar lb a convertir : "))
        kg=lb*0.453592
        print(f"el valor de lb a kg es de {kg} ")

    elif N==5:
        c=int(input("favor ingresar c° a convertir : "))
        f=(c*9/5)+32
        print(f"el valor de c° a f° es de {f}")
    elif N==6:
        f=int(input("favor ingresar f° a convertir : "))
        c=(f-32)*5/9
        print(f"el valor de f° a c° es de {c}")
    elif N==7:
        break


