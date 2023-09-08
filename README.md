# DIO_Sistema_Bancario_Python_Version2
 
# Sistema Bancário em Python - Versão 2.0

Este é um projeto de sistema bancário em Python que permite aos usuários realizar operações de depósito, saque, visualizar histórico, criar usuários (clientes) e criar contas correntes.
proposta do Prof. Guilherme Carvalho - Python Consultant, Oak Solutions (https://github.com/guicarvalho)

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

- Criar Usuário: Os usuários podem ser cadastrados com nome, data de nascimento, CPF e endereço. CPFs duplicados não são permitidos.
- Criar Conta Corrente: Contas correntes podem ser criadas e associadas a um usuário. O número da conta é sequencial e único.
- Depositar: Os usuários podem fazer depósitos em suas contas correntes.
- Sacar: Os usuários podem realizar saques de suas contas correntes com limite diário e controle de número de saques.
- Visualizar Histórico: Os usuários podem visualizar o histórico de transações de suas contas correntes.

## Instruções de Uso

1. Clone o repositório para sua máquina local:

```bash
   git clone https://github.com/otavioaugust1/DIO_Sistema_Bancario_Python_Version2.git
```


2. Navegue até o diretório do projeto:

```bash
    cd nome-do-repositorio
```

3. Execute o programa Python:

```bash
    python sistema_bancario_2.py
```

4. Siga as instruções no console para realizar as operações desejadas.

## Exemplo de Uso
Aqui estão alguns exemplos de uso do programa:

* Criar Usuário:

```bash
    ### Menu ###
    1. Criar Usuário
    2. Criar Conta Corrente
    3. Depositar
    4. Sacar
    5. Visualizar Histórico
    6. Sair
    Digite o número da operação desejada: 1
    Digite o nome do usuário: João da Silva
    Digite a data de nascimento do usuário: 01/01/1990
    Digite o CPF do usuário: 123.456.789-00
    Digite o endereço do usuário (formato: logradouro, nro ; bairro - cidade/sigla estado): Rua Principal, 123 ; Centro - São Paulo/SP
```

* Criar Conta Corrente:

```bash
    ### Menu ###
    1. Criar Usuário
    2. Criar Conta Corrente
    3. Depositar
    4. Sacar
    5. Visualizar Histórico
    6. Sair
    Digite o número da operação desejada: 2
    Digite o CPF do titular da conta: 123.456.789-00
    Conta criada com sucesso. Número da Conta: 1
```
* Depositar:

```bash
    ### Menu ###
    1. Criar Usuário
    2. Criar Conta Corrente
    3. Depositar
    4. Sacar
    5. Visualizar Histórico
    6. Sair
    Digite o número da operação desejada: 3
    Digite o número da conta: 1
    Digite o valor do depósito: 1000.00
```

* Sacar:

```bash
    ### Menu ###
    1. Criar Usuário
    2. Criar Conta Corrente
    3. Depositar
    4. Sacar
    5. Visualizar Histórico
    6. Sair
    Digite o número da operação desejada: 4
    Digite o número da conta: 1
    Digite o valor do saque: 300.00
```
Visualizar Histórico:

```bash
    ### Menu ###
    1. Criar Usuário
    2. Criar Conta Corrente
    3. Depositar
    4. Sacar
    5. Visualizar Histórico
    6. Sair
    Digite o número da operação desejada: 5
    Digite o número da conta: 1
    ### Histórico ###
    Depósito: +RS 1000.00
    Saque: -RS 300.00
    Saldo atual: RS 700.00
```

## Contribuição
Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está sob a Licença MIT.











