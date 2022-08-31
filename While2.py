num = 10
print("DESCUBRA")

while True:
    palpite = int(input("Tente acertar o número: "))
    if palpite > num:
        print("Seu palpite é maior! ")
        continue
    elif palpite < num:
        print("Seu palpite é menor! ")
        continue
    else:
        print(f"{palpite} é o número secreto! Acertou! ")
        break
