def real (dolar,cotacao):
    return dolar*cotacao

cotacao = float(input ("Insira a cotação atual do dolar: "))
dolar = float(input("Insira quantos dólares você tem, e eu te digo quantos reais possui: "))

print(f"Você tem R$ {real(dolar,cotacao):.2f} reais.")