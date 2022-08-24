timeA = input("Informe o nome do time : ")
placarA = int(input(f"Informe o placar do  {timeA}: "))
timeB = input("Informe o nome do time : ")
placarB = int(input(f"Informe o placar do  {timeB}: "))

if placarA > placarB:
    print(f"Placar: {timeA} {placarA} x {placarB} {timeB}. O {timeA} Venceu! ")
elif placarA < placarB:
    print(f"Placar: {timeA} {placarA} x {placarB} {timeB}. O {timeB} Venceu! ")
else:
    print(f"Placar: {timeA} {placarA} x {placarB} {timeB}. Empate! ")