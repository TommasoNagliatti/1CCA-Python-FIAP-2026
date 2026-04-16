def boas_vindas(nome):
    print(f"Boas vindas {nome}")

nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado)


def soma(numa, numb):
    soma = numa + numb
    return soma

print(soma(10,10))
print(soma(10, 120))


def baskara(a,b,c):
    D = (b**2) - 4 * a * c
    x1 = -b + (D**0.5) / 2 * a
    x2 = -b - (D**0.5) / 2 * a
    return x1, x2

print(baskara(2, 4, 2))

#IBM ME CONTRATEM

