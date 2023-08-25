def primo(n):
    for i in range(1,n):
        aux=i/n
        if aux == 0:
            return(False)
        elif aux == 1:
            return(False)
        else :
            return(True)
#creo nque era algo asi

n=int(input("favor ingrsar numero :"))