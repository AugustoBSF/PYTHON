precoGasosa = 6.50
precoAlcool = 5.00
desconto_alcool = 0.05  


combustivel = input("Você abasteceu com álcool ou gasolina? ")

if combustivel == "gasolina":
    precoFinal = precoGasosa
    print(f"O preço final da gasolina é: R${precoFinal:.2f}")

elif combustivel == "álcool":
    precoFinal = precoAlcool * (1 - desconto_alcool) 
    print(f"O preço final do álcool com desconto é: R${precoFinal:.2f}")

else:
    print("Tipo de combustível inválido.")
