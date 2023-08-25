
def palindromo(p):
    palabra.strip(' ')
    arbalap=palabra[::-1]
    if palabra == arbalap:
        return(True)
    else:
        return(False)

palabra=str(input("ingresar palabra : "))
if palindromo == True:
    print("la palabra esocjida es palindroma")
elif palindromo == False:
    print("la palabra escojida no es palindroma")
    
