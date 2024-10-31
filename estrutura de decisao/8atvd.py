lado1 = float(input("Informe o primeiro lado: "))
lado2 = float(input("Informe o segundo lado: "))
lado3 = float(input("Informe o terceiro lado: "))

if (lado1 == lado2 == lado3):
    resultado = "equilátero"
elif(lado1 != lado2 != lado3):
    resultado = "escaleno"
else: 
    resultado = "isósceles"

print(f"O triangulo é: {resultado}")