# Para rodar cada exercício é necessário comentar todos os demais
# Atalho pra comentar trecho selecionado: Shift + Alt + A

# 1)
print("Alo mundo")

# 2)
numero = float(input("Digite um número: "))
print(f"O número informado foi {numero}")

# 3)
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print(f"Soma: {num1 + num2}")

# 4)
i = notaTotal = 0
while (i < 4):
    nota = float(input("Digite uma nota: "))
    notaTotal += nota
    i += 1

media = notaTotal / 4
print(f"Média das notas: {media}")

# 5)
metro = float(input("Digite um número (metros): "))
centimetros = metro * 100
print(f"{metro}m são {centimetros}cm")

# 6)
pi = 3.14
raio = float(input("Digite o raio do círculo: "))
area = pi * (raio ** 2)
print(f"Área do círculo: {area}")

# 7)
lado = float(input("Digite o lado do quadrado: "))
area = lado * lado
print(f"Resultado: {area * 2}")

# 8)
valorHora = float(input("Digite quanto ganha por hora: "))
horasT = float(input("Horas trabalhadas no mês: "))
salario = valorHora * horasT
print(f"Salário: {salario}")

# 9)
fahrenheit = float(input("Temperatura em Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)
print(f"{fahrenheit}°F são {celsius}°C")

# 10)
celsius = float(input("Temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C são {fahrenheit}°F")

# 11)
numInt1 = int(input("Digite o primeiro número inteiro: "))
numInt2 = int(input("Digite o segundo número inteiro: "))
numR = float(input("Digite um número real: "))

problema1 = (numInt1 * 2) + (numInt2 / 2)
print(f"\nO produto do dobro do primeiro com metade do segundo: {problema1}")
problema2 = (numInt1 * 3) + numR
print(f"A soma do triplo do primeiro com o terceiro: {problema2}")
problema3 = numR ** 3
print(f"O terceiro elevado ao cubo: {problema3}")

# 12)
giga = float(input("Digite um valor em Gigabytes: "))
mega = giga * 1024
print(f"{giga}GB são {mega}MB")

# 13)
giga = float(input("Digite um valor em Gigabytes: "))
mega = giga * 1024
kilo = giga * 1024 * 1024
print(f"{giga}GB são {mega}MB ou {kilo}KB")