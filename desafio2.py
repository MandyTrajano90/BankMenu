def menu():
    menu = """
    ************MENU************

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Nova Conta
        [5] Listar Contas
        [6] Novo Cliente
        [7] Filtrar Cliente
        [8] Sair 

    ****************************

        """
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido.")
    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > limite:
        print("Valor maior que o limite.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif numero_saques >= limite_saques:
        print("Limite de saques diários atingido.")
    else:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
    return saldo, extrato

def exibir_extrato():

def criar_cliente():

def filtrar_cliente():

def criar_conta():  


def listar_contas():


def main():
saldo = 0
limite = 500
limite_diario = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
clientes = []
contas = []

while True:

    opcao = menu()

    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: R$"))
        saldo, extrato = depositar(saldo, valor, extrato)
     
    
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

main()