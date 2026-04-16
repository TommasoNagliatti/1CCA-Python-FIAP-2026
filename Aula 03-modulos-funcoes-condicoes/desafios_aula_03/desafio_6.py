numbera = int(input("Coloque um numero: "))
oper = input("coloque um operador (*, /, +, -): ")
numberb = int(input("Coloque um outro numero: "))

if oper == "+":
   resultado = numbera + numberb

elif oper == "-":
    resultado = numbera - numberb

elif oper == "*":
    resultado = numbera * numberb

elif oper == "/":
    resultado = numbera / numberb

else:
    print("Operador invalido")

print(f" resultado da conta {numbera} {oper} {numberb} é: {resultado}")