# Calculadora Básica

num1 = float(input("Digite o primeiro número: "))
operador = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

if operador == "+":
    print("Resultado:", num1 + num2)
elif operador == "-":
    print("Resultado:", num1 - num2)
elif operador == "*":
    print("Resultado:", num1 * num2)
elif operador == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Erro: divisão por zero")
else:
    print("Operação inválida")


# Registro de Notas e Média da Turma

quantidade = int(input("\nQuantos alunos há na turma? "))
soma = 0

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    soma += nota

media = soma / quantidade
print("Média da turma:", media)


# Verificador de Senha Segura

senha = input("\nDigite uma senha: ")
tem_numero = False

for c in senha:
    if c.isdigit():
        tem_numero = True

if len(senha) >= 8 and tem_numero:
    print("Senha válida")
else:
    print("Senha inválida")


# Analisador de Números (Par ou Ímpar)

pares = 0
impares = 0

quantidade = int(input("\nQuantos números deseja digitar? "))

for i in range(quantidade):
    numero = int(input(f"Digite o número {i + 1}: "))

    if numero % 2 == 0:
        print("Par")
        pares += 1
    else:
        print("Ímpar")
        impares += 1

print("Pares:", pares)
print("Ímpares:", impares)
