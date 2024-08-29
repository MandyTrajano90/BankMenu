def menu():
    menu = """
    ************MENU************

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Nova Conta
        [5] Listar Contas
        [6] Novo Cliente
        [7] Sair 

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


def exibir_extrato(saldo, /, *,  extrato):
    print("##### EXTRATO #####")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R${saldo:.2f}\n")
    print("###################")


def novo_cliente(cliente):
    cpf = input("Digite o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Cliente já cadastrado!")
        return 

    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço: ")
    cliente = {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco}
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")
    

def filtrar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None


def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Digite o CPF do cliente (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}

    print("Cliente não encontrado.")


def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Número da conta: {conta['numero_conta']}")
        print(f"Cliente: {conta['cliente']['nome']}")
        print("-------------------------------")

def sair():
    print("Saindo...")


def main():
    print("Bem-vindo ao Banco DevPro!")
    print("O que deseja fazer?")
saldo = 0
limite = 500
limite_diario = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = '0001'
clientes = []
contas = []

while True:

    opcao = menu()

    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: R$"))
        saldo, extrato = depositar(saldo, valor, extrato)
     
    
    elif opcao == "2":
            valor = float(input("Digite o valor a ser sacado: R$"))
            saldo, extrato = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)


    elif opcao == "4":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, clientes)

        if conta:
            contas.append(conta)
    
    elif opcao == "5":
        listar_contas(contas)
    
    elif opcao == "6":
        novo_cliente(clientes)

    elif opcao == "7":
        sair()
        break
    
    else:
        print("Opção inválida.")

main()