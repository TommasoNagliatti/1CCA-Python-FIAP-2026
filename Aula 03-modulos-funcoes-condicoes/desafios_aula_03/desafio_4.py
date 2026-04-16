nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))
nota3 = int(input('Digite sua terceira nota: '))
nota4 = int(input('Digite sua quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A media do aluno foi: {media}")

if media >= 7:
    print("aluno aprovado")

elif media > 4 and media < 7:
    print("aluno em recuperacao")

else:
    print("aluno reprovado")
