# Cálculo de Gorjeta

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)


# Verificador de Palíndromo

def eh_palindromo(texto):
    texto = texto.lower()
    texto = "".join(c for c in texto if c.isalnum())
    return texto == texto[::-1]


# Menu Principal

print("1 - Calcular gorjeta")
print("2 - Verificar palíndromo")
print("3 - Calcular desconto")
print("4 - Calcular dias vividos")

opcao = input("Escolha uma opção: ")

# Gorjeta
if opcao == "1":
    valor = float(input("Digite o valor da conta: "))
    porcentagem = float(input("Digite a porcentagem da gorjeta: "))
    print("Valor da gorjeta:", calcular_gorjeta(valor, porcentagem))


# Palíndromo
elif opcao == "2":
    frase = input("Digite uma palavra ou frase: ")

    if eh_palindromo(frase):
        print("Sim")
    else:
        print("Não")


# Cálculo de Desconto
elif opcao == "3":
    preco = float(input("Digite o preço do produto: "))
    desconto = float(input("Digite o desconto (%): "))

    valor_desconto = preco * (desconto / 100)
    preco_final = preco - valor_desconto

    print(f"Preço final: R$ {preco_final:.2f}")


# Cálculo de Dias Vividos
elif opcao == "4":
    from datetime import date

    ano = int(input("Ano de nascimento: "))
    mes = int(input("Mês de nascimento: "))
    dia = int(input("Dia de nascimento: "))

    data_nascimento = date(ano, mes, dia)
    data_atual = date.today()

    dias_vivos = (data_atual - data_nascimento).days

    print("Dias vividos:", dias_vivos)

else:
    print("Opção inválida")
