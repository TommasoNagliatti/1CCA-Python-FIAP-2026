'''Faça um programa que exiba a mensagem “Olá, Mundo”.
Essa mensagem deverá ser exibida repetidamente.
Ao final de toda iteração da repetição, você deve perguntar ao usuário se ele deseja exibir a mensagem novamente.
Se sim, exiba novamente. Senão, saia do loop e exiba a mensagem “Fim”.'''

print("hello World")
repetir = "sim"

while repetir.lower() == "sim":
    repetir = input("deseja ver a mensagem novamente? [sim/nao] ")
    print("inicia ou repete o jogo")

print("fim da repeticao")