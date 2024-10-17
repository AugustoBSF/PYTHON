mediaPassar = 7

nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))

mediaAluno = (nota1 + nota2) /2

if mediaAluno >= mediaPassar:
    print("Aprovado. ")
else:
    print("Reprovado. ")