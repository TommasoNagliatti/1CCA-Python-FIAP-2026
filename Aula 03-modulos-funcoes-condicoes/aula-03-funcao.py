
#ESTRUTURA CONDICIONAL SIMPLES
nota = 7.0

if nota < 6:
    print("Sua nota é:", nota)

print("FIM")
#fim

#ESTRUTURA CONDICIONAL COMPOSTA
nota_final = 5.0

if nota_final < 6:
    print("Reprovado")
else:

    print("Aprovado")

print("FIM")
#fim

#ESTRUTURA CONDICIONAL ENCADEADA
nota_final = 7.0

if nota_final < 4:
    print("Reprovado")
else:
    if nota_final < 6:
        print("Recuperação")
    else:
        print("Aprovado")

print("FIM")
#fim

#ESTRUTURA CONDICIONAL COMPOSTA – ELIF
nota_final = 2.0

if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")

print("FIM")
#fim

#NÃO // ! // Terá valor falso quando a proposição for verdadeira e vice-versa.
#E  // && // Será verdadeira somente quando todas as preposições forem verdadeiras.
#OU // || // Será verdadeira quando pelo menos uma das preposições for verdadeira.

nota_final = 7.0

prep1 = nota_final >= 5 # True
prep2 = nota_final < 7 # False

logica_e = prep1 and prep2 # False
logica_ou = prep1 or prep2 # True