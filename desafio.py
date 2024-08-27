menu = """
******MENU******

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

*****************
=> """
# Variáveis
saldo = 0
limite = 500
limite_diario = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Verificações
while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: R$"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Valor inválido.")
    
    elif opcao == "2":
            valor = float(input("Digite o valor a ser sacado: R$"))
            if valor > limite:
                print("Valor maior que o limite.")
            elif valor > saldo:
                print("Saldo insuficiente.")
            elif numero_saques >= LIMITE_SAQUES:
                print("Limite de saques diários atingido.")
            else:
                saldo -= valor
                extrato += f"Saque: R${valor:.2f}\n"
                numero_saques += 1

    elif opcao == "3":
        print("##### EXTRATO #####")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}\n")
        print("###################")
    
    elif opcao == "4":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida.")
