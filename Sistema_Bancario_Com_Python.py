menu = """ 

 [1] Extrato
 [2] Depositar
 [3] Sacar
 [0] Sair

 => """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 5

while True:

    opcao = input(menu)

    if opcao == "1":
        print("\n~~~~~~~~~~ EXTRATO ~~~~~~~~~~")
        print("Não foram realiadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    elif opcao == "2":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("FALHA NA OPERAÇÃO! O valor informado é inválido.")

    elif opcao == "3":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("FALHA NA OPERAÇÃO! Saldo insuficiente na conta.")

        elif excedeu_limite:
            print("FALHA NA OPERAÇÃO! Valor do saque maior que limite permitido de saque.")

        elif excedeu_saques:
            print("FALHA NA OPERAÇÃO! Excedeu máximo de saques diários permitidos.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("FALHA NA OPERAÇÃO! O valor informado é inválido.")


    elif opcao == "0":
        break
    
    else:
        print("FALHA NA OPERAÇÃO! Porfavor selecione novamente a operação desejada.")
        print("Em caso de duvidas consulte um de nossos atendentes.")