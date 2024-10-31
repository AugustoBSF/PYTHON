preco = float(input("Informe o valor do produto: R$"))

if (preco > 100): 
    preco = preco * 0.9

print(f"Novo valor com desconto: R${preco:.2f}")