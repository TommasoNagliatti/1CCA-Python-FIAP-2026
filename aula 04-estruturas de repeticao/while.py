#while repeticao
cp = 1
while cp <= 3:
    print(cp)
    cp += 1

print()

#while decrescente de 4 ate 1 (incluindo)
cp = 4
while cp > 0:
    print("Produto", cp)
    cp -= 1

# repeticao com entrada do usario
jogar = "sim"

while jogar.lower() == "sim":
    print("inicia ou repete o jogo")
    jogar = input("deseja jogar novamente?")