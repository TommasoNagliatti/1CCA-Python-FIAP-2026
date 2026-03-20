from lxml.html.builder import INPUT

print("Oi Tommaso")

print("7 + 4 =" , 7+4)
print("7"+"4") #CONCATENAÇÃO DE STRINGS

# comentário de 1 linha

'''
comentarios
de
multiplas 
linhas
'''

# VARIAVEIS
nome = "Tommaso" #str
idade = 20 #int
peso = 80 #float

print (f"nome: {nome}",f"idade: {idade}",f"peso: {peso}")
print(f"Oiii {nome}!!!")

# INPUT - Simulação de um forms no CMD
nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade "))

nova_idade = idade + 1

print (nome, idade)
print (nova_idade)
