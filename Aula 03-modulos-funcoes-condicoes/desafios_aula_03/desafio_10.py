a = int(input("digite o valor do lado a: "))
b = int(input("digite o valor do lado b: "))
c = int(input("digite valor do lado c: "))

if a > b and a > c:

    if b > c:
        print("os valores em ordem decrescente:")
        print("respectivamente a, b, c:")
        print(a, b, c)

    else:
        print("os valores em ordem decrescente:")
        print("respectivamente a, c, b:")
        print(a, c, b)

elif b > a and b > c:

    if c > a:
        print("os valores em ordem decrescente:")
        print("respectivamente b, c, a:")
        print(b, c, a)
    else:
        print("os valores em ordem decrescente:")
        print("respectivamente b, a, c:")
        print(b, a, c)

elif c > a and c > b:

    if b > a:
        print("os valores em ordem decrescente:")
        print("respectivamente c, b, a:")
        print(c, b, a)
    else:
        print("os valores em ordem decrescente:")
        print("respectivamente c, a, b:")
        print(c, a, b)
else:
    print("respectivamente a, b, c:")
    print(a, b, c)

#verificar se é ou nao um triangulo
if abs(b-c) < a < b+c and abs(a-c) < b + a+c and abs(a-b) < c < a+b:

    if (a ** 2) == (b ** 2) + (c ** 2):
        print("TRIANGULO RETANGULO")

    elif (a ** 2) > (b ** 2) + (c ** 2):
        print("TRIANGULO OBTUSANGULO")

    elif (a ** 2) < (b ** 2) + (c ** 2) and a != b and c != b:
        print("TRIANGULO ACUTANGULO")

    elif a == b and c == a and b == c:
        print("TRIANGULO EQUILATERO")

    elif a == b or a == c or b == c:
        print("TRIANGULO ISOCELES")

else:
    print("NAO FORMA TRIANGULO")

