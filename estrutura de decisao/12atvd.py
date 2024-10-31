
n1 = float(input("Digite o primeiro número: "))


n2 = float(input("Digite o segundo número: "))


operador = input("Digite o operador (+, -, *, /): ")


if operador == "+":
    resultado = n1 + n2
    print(f"O resultado de {n1} + {n2} = {resultado}")
elif operador == "-":
    resultado = n1 - n2
    print(f"O resultado de {n1} - {n2} = {resultado}")
elif operador == "*":
    resultado = n1 * n2
    print(f"O resultado de {n1} * {n2} = {resultado}")
elif operador == "/":
    if n2 == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        resultado = n1 / n2
        print(f"O resultado de {n1} / {n2} = {resultado}")
else:
    print("Operador inválido.")
