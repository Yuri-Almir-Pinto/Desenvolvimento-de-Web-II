def Imc(peso, altura):
    return peso/(altura*altura)
altura = float(input("Digite a sua altura em metros: "))
peso = float(input("Digite o seu peso em kg: "))

print(f"Seu IMC é igual a: {Imc(peso,altura):.2f}")