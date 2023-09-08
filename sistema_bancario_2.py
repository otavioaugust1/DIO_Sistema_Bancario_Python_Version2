# Variáveis globais
usuarios = []
contas = []
numero_conta_sequencial = 1
numero_saques = {}  # Dicionário para rastrear o número de saques por conta

# Função de saque
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= saldo and valor <= limite and numero_saques < limite_saques:
        saldo -= valor
        extrato.append(f"Saque: -RS {valor:.2f}")
        numero_saques += 1
    else:
        print("Saque não permitido. Verifique o valor, saldo disponível ou limite de saques.")
    return saldo, extrato

# Função de depósito
def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: +RS {valor:.2f}")
    else:
        print("O valor do depósito deve ser positivo.")
    return saldo, extrato

# Função para exibir histórico
def visualizar_historico(saldo, /, *, extrato):
    print("### Histórico ###")
    for transacao in extrato:
        print(transacao)
    print(f"Saldo atual: RS {saldo:.2f}")

# Função para criar usuário
def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    endereco = input("Digite o endereço do usuário (formato: logradouro, nro ; bairro - cidade/sigla estado): ")
    
    # Verifica se o CPF já existe na lista de usuários
    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            print("CPF já cadastrado. Não é possível cadastrar o mesmo CPF novamente.")
            return
    
    usuarios.append({"Nome": nome, "Data de Nascimento": data_nascimento, "CPF": cpf, "Endereço": endereco})

# Função para criar conta corrente
def criar_conta_corrente(usuario):
    global numero_conta_sequencial
    agencia = "0001"
    numero_conta = numero_conta_sequencial
    numero_conta_sequencial += 1
    conta = {"Agência": agencia, "Número da Conta": numero_conta, "Titular": usuario, "Saldo": 0.0, "Extrato": []}
    contas.append(conta)
    print(f"Conta criada com sucesso. Número da Conta: {numero_conta}")

# Função principal
def main():
    while True:
        print("\n### Menu ###")
        print("1. Criar Usuário")
        print("2. Criar Conta Corrente")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Visualizar Histórico")
        print("6. Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            cpf = input("Digite o CPF do titular da conta: ")
            usuario = None
            for u in usuarios:
                if u["CPF"] == cpf:
                    usuario = u
                    break
            if usuario is not None:
                criar_conta_corrente(usuario)
            else:
                print("Usuário não encontrado. Crie o usuário primeiro.")
        elif opcao == "3":
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do depósito: "))
            for conta in contas:
                if conta["Número da Conta"] == numero_conta:
                    conta["Saldo"], conta["Extrato"] = deposito(conta["Saldo"], valor, conta["Extrato"])
                    break
            else:
                print("Conta não encontrada.")
        elif opcao == "4":
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do saque: "))
            for conta in contas:
                if conta["Número da Conta"] == numero_conta:
                    conta["Saldo"], conta["Extrato"] = saque(
                        saldo=conta["Saldo"],
                        valor=valor,
                        extrato=conta["Extrato"],
                        limite=500.0,
                        numero_saques=numero_saques.get(conta["Número da Conta"], 0),
                        limite_saques=3
                    )
                    break
            else:
                print("Conta não encontrada.")
        elif opcao == "5":
            numero_conta = int(input("Digite o número da conta: "))
            for conta in contas:
                if conta["Número da Conta"] == numero_conta:
                    visualizar_historico(saldo=conta["Saldo"], extrato=conta["Extrato"])
                    break
            else:
                print("Conta não encontrada.")
        elif opcao == "6":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
