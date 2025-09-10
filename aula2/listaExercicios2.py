# Para rodar cada exercício é necessário comentar todos os demais
# Atalho pra comentar trecho selecionado: Shift + Alt + A

# 1)
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("Número par")
else:
    print("Número ímpar")

# 2)
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# 3)
idade = int(input("Digite sua idade: "))
if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")

# 4)
lado1 = int(input("Insira o primeiro lado do triângulo: "))
lado2 = int(input("Insira o segundo lado do triângulo: "))
lado3 = int(input("Insira o terceiro lado do triângulo: "))

if (lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1):
    if (lado1 == lado2 and lado2 == lado3):
        print("Triângulo equilátero")
    elif (lado1 == lado2 or lado2 == lado3 or lado1 == lado3):
        print("Triângulo isóceles")
    else:
        print("Triângulo escaleno")
else:
    print("Não é um triângulo")

# 5)
numero = int(input("Digite um número: "))
if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Zero")

# 6)
nota = int(input("Digite sua nota: "))
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# 7)
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if a == 0:
    print("Não é do segundo grau")
else:
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print("Não existem raízes reais")
    elif delta == 0:
        print("Existe uma raiz real")
    else:
        print("Existem duas raízes reais")