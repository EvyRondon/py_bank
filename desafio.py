menu = """"
[d] depositar
[s] sacar
[e] extrato
[q] sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito \n"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"
        else:
            print("A operação falhou! O valor informado é inválido.")
    elif opcao == "s":
        valor = float(input("Informa o valor do saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu limite.")

        elif excedeu_limite:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"\n Saque: R${valor:.2f}\n"
            numero_saque +=1
    elif opcao == "e":  
        print("\n============ Extrato ===========")  
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("===================================")
    
    elif opcao == "q":
      break

    else:
      print("Operação inválida, por favor selecione novamente a opção desejada.")