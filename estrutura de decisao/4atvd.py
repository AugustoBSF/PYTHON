idade = int (input("Digite sua idade: "))
if idade < 18 and idade >= 0:
    print("Menor de idade. ")
elif idade >= 18 and idade <=60:
     print ("Adulto")
else:
    print("Idoso")