nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    while media < 10:
        print("ALUNO APROVADO")
        media += 1

elif media <= 5:
    while media <= 10:
        print("ALUNO REPROVADO")
        media += 1

