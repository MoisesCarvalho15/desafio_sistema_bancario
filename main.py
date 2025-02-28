menu = """ Bem vindo ao Sistema Bancário v1

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Digite a opção desejada através do número ou o nome da operação.
"""

saldo = 0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(menu)
    opcao = input("=>: ").lower()

    if opcao == "1" or opcao  == 'depositar':
        valor = float(input("Informe somente o valor do depósito: R$ "))
        saldo += valor
        extrato += f"| + Depósito: R$ {valor:.2f}\n"
        print("\nDepósito feito com sucesso.\nVoltando para o menu principal.\n")
        

    elif opcao == "2" or opcao  == 'sacar':
        valor = float(input("Informe somente o valor do saque: R$ "))
        
        if valor > limite_valor_saque:
            print(f"\nO valor excedeu o seu limite por saque.\nValor por saque: R$ {limite_valor_saque}")
            print("Voltando ao menu principal.\n")
       
        elif (valor <= limite_valor_saque) and (valor <= saldo) and (numero_saques < LIMITE_SAQUES):
            saldo -= valor
            numero_saques += 1
            extrato += f"| - Saque: R$ {valor:.2f}\n"
        
            print("\nSaque efetuado com sucesso.\nVoltando ao menu principal.\n")
        
        elif valor > saldo: 
            print("\nValor do saque é maior do que o saldo disponível.\nVoltando ao menu principal.\n")
        
        else:
            print("\nVocê já excedeu seu limite de saques hoje.\nVoltando ao menu principal.\n")
    
    elif opcao == "3" or opcao  == 'extrato':
        print(f"{10 * '#'} Extrato {10 * '#'}")
        
        if extrato == "":
            print("| * Não foram realizadas movimentações.")
        else:
            print(f"{extrato}\n| = Saldo: R$ {saldo:.2f}")
            
        print(f"{29 * '#'}\n")
    
    elif opcao == "4" or opcao  == 'sair':
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
