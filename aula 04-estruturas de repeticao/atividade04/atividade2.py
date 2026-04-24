def validar_nota(nota):
    while nota < 0 or nota > 10:
        print("nota invalida, deve ser entre 0 e 10")
        nota = float(input("Digite novamente: "))
    return nota

notaA = float(input("Digite a primeira nota: "))
notaA = validar_nota(notaA)

notaB = float(input("Digite a segunda nota: "))
notaB = validar_nota(notaB)

media = (notaA + notaB) / 2
print(media)