salario = float(input("Digite o salário do funcionário: "))


if salario < 1000:
    aumento = salario * 0.10  
else:
    aumento = salario * 0.05  


novoSalario = salario + aumento

# Exibe o resultado
print(f"O aumento é: R${aumento:.2f}")
print(f"O novo salário é: R${novoSalario:.2f}")
