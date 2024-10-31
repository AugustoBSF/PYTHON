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