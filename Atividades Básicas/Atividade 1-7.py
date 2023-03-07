def salario (horas, ganho):
    return horas*ganho

horas = int(input("Digite a quantidade de horas trabalhadas no mês: "))
ganho = float(input("Digite o quanto você ganha por hora em reais: "))

print (f"Seu salário total no mês é de R$ {salario(horas,ganho):.2f} reais.")