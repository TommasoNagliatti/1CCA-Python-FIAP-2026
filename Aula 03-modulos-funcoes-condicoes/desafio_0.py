idade = int(input("Qual a sua idade?"))

if idade > 18 and idade < 70:
    print("Você é obrigado a votar, ou pague uma multa")

elif idade >= 70 or idade <= 18 and idade > 15:
    print("Você não tem obrigação de votar, mas pode.")

else:
    print("Você não pode votar, aproveite enquanto ainda é jovem")