while True:
    numeroTeste = int(input("Digite um número (999 para finalizar o programa): "))

    if numeroTeste == 999:
        print("Programa finalizado.")
        break

    if numeroTeste % 2 == 0:
        print(f"O número {numeroTeste} é Par!")
    else:
        print(f"O número {numeroTeste} é Ímpar!")