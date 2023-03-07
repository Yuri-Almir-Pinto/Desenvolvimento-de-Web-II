def conversao (grausF):
    return  float(5 * ((grausF-32) / 9))

grausF = float(input("Digite os graus em Fahrenheit: "))

print (f"Isso da {conversao(grausF):.1f} Graus Celsius.")