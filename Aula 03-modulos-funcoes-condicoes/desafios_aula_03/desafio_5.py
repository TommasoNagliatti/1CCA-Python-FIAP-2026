na = int(input("Escolhe um numero inteiro positivo: "))
nb = int(input("Escolhe um outro numero inteiro positivo: "))

if na > nb:
    resultado = na % nb

    if resultado == 0:
        print("sao multiplos")

    else:
        print("nao sao multiplos")

else:
    resultado = nb % na

    if resultado == 0:
        print("sao multiplos")

    else:
        print("nao sao multiplos")
