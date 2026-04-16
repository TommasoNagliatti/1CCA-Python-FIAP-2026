nome = input("Digite o nome do colaborador: ")
salario = int(input(f"digite o salario do {nome}: "))

print(f"========tabela final do colaborador {nome}:========")
print(f"salario antes do reajuste: R$ {salario}")
if salario <= 280:
    aumento = salario * 0.2
    salario_final = salario + aumento
    print("houve um aumento de 20%")

elif salario > 280 and salario <= 700:
    aumento = salario * 0.15
    salario_final = salario + aumento
    print("houve um aumento de 15%")

elif salario > 700 and salario <= 1500:
    aumento = salario * 0.10
    salario_final = salario + aumento
    print("houve um aumento de 10%")

elif salario > 1500:
    aumento = salario * 0.05
    salario_final = salario + aumento
    print("houve um aumento de 5%")

print(f"valor do reajuste: R$ {aumento}")
print(f"salario depois do reajuste: R$ {salario_final}")
print("===================================================")