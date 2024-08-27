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

# Funções
while True
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: R$"))
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
    
    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor a ser sacado: R$"))
            if valor <= saldo + limite_diario:
                saldo -= valor
                extrato += f"Saque: R${valor:.2f}\n"
                numero_saques += 1
            else:
                print("Saldo insuficiente.")
    elif opcao == "3":
        print("##### EXTRATO #####")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}\nLimite: R${limite:.2f}\n{extrato}")
        print("###################")
    
    elif opcao == "4":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida.")
