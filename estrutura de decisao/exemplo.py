"""
idade = int (input ("Digite sua idade: "))

if idade > 17:
    print ("Entrada permitdida.")
else: 
        print ("Entrada proibida.")
"""

"""
num = int(input("Digite um número: "))
if num > 0 :
    print("Número é positivo.")
elif num < 0 :
    print("Número é negativo.") 
else:
    print("Número é neutro.")
"""
"""
num = int(input("Digite um número: "))
if num % 2 == 0:
    print ("numero é par. ")
else:
        print ("numero é impar. ")
"""
"""
ano = int(input("Digite um número: "))
if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)):
    print("Ano bissexto.")
else:
    print ("Ano normal. ")
    """
"""
altura = float(input ("Digite a sua altura: "))
peso = float(input ("Digite a sua peso em Kg: "))

imc = peso/(altura**2)

if (imc < 18.5):
    print ("Abaixo do peso normal. ") 

elif (imc >= 18.5 and imc <= 24.9 ):
    print ("Peso normal. ")

elif (imc >= 25 and imc <= 29.9 ):
    print*- ("Sobrepeso. ")
else:
    print("Obesidade grau I")
    """