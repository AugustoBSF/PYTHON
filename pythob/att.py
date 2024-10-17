nome = input ("Insira seu nome: ")
idade = int (input ("Insira sua idade: "))
peso = float (input ("Insira seu peso: "))

#antiga
# print ("%s tem %d anos de idade e %.2fKg" % (nome,idade,peso))

#nova
# print("{} tem {} anos de idade e {:.2f}Kg".format (nome,idade,peso) ) 

#super nova

print (f"{nome} tem {idade} anos de idade e {peso:.2f}Kg")