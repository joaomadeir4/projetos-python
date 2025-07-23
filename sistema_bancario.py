import textwrap

def menu():
    menu = """\n
    Seja bem-vindo ao Banco DIO, escolha uma das opções desejadas: 
    
    :::::::::::::::::::::::::: MENU ::::::::::::::::::::::::::  
    OPERAÇÕES PARA CONTA OU USUÁRIO:
    [1] Novo Usuário
    [2] Nova Conta
    [3] Listar Contas
    
    OPERAÇÕES BANCÁRIAS: 
    [4] Depositar
    [5] Sacar
    [6] Extrato
    
    FINALIZAR OPERAÇÃO: 
    [7] Sair
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    => """
    
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato,/):
    if valor > 0: 
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nSeu saldo atual é de R${saldo:.2f}")

    else:
        print("Operação falhou! O valor informado é inválido")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print(f"Operação falhou! O valor é maior que o limite permitido. Limite R${limite:.2f}")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0: 
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\nSeu saldo atual é de R${saldo:.2f}")
        
        else:
            print("Operação falhou! O valor informado é inválido.")
            
        return saldo, extrato, numero_saques
    
def exibir_extrato(saldo, numero_saques, limite_saques, / , * , extrato):
    print("\n-------------------- EXTRATO BANCÁRIO --------------------")
        
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(f"{extrato}")
        print("\n------------------------------------------------------------")
    print(f"\nSaldo: R$ {saldo:.2f}")
    
    print(f"Número de saques hoje: {numero_saques} | Limite de Saques: {limite_saques}")
    
    print("------------------------------------------------------------")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nJá existe um usuário com o CPF cadastrado.")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (Logradouro, Número, Bairro, Cidade/Sigla do Estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento:": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuário criado com sucesso!")       
    
def filtrar_usuario(cpf, usuarios):  
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, fluxo de criação de conta encerrado.")
    
def listar_contas(contas):
    
    if not contas:
        print("Não há contas cadastradas, seja nosso primeiro Cliente!")
    else: 
        for conta in contas:
            linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            
            """
            print("=" * 100)
            print(textwrap.dedent(linha))
        
        
       
def main():
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""

    numero_saques = 0
    limite_saques = 3

    contas = []
    usuarios = []

    while True:
        opcao = menu()
        
        if opcao == "1":#Criar usuário
            criar_usuario(usuarios)
            
        elif opcao == "2": #Criar Conta
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
            
        elif opcao == "3": #Listar Contas
            listar_contas(contas)
            
        elif opcao == "4": #Depósito
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "5": #Saque
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques,
            )

        elif opcao == "6": #Extrato
            exibir_extrato(saldo, numero_saques, limite_saques, extrato=extrato)
        
        elif opcao == "7": #Sair
            print("Você encerrou a operação. Obrigado por ser nosso Cliente.")
            break
            
        else:
            print("Operação inválida, por favor, selecione uma das opções apresentadas.")
            
main()
