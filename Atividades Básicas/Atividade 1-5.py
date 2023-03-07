def conceito (conceito):
    if conceito == 'A':
        return 10
    elif conceito == 'B':
        return 8.5
    elif conceito == 'C':
        return 6
    elif conceito == 'D':
        return 4
    else:
        print ("Valor inputado inválido.")
        return "WRONG"

con = str(input("Digite a sua nota (A, B, C ou D):" ))
if conceito(con) != 'WRONG':
    print(f"Sua nota final é {conceito(con):.1f}")

