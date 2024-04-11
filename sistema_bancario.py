menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair


=> """

saldo = 0
limite = 500 
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  opcao = input (menu)

  if opcao == "1":
   valor = float(input("\nQual o valor a ser depositado: "))
   print(f"\nSeu deposito de R$ {valor} foi realizado com sucesso!")
  
   if valor > 0:
     saldo += valor
     extrato += f"Deposito: R$ {valor:.2f}\n"

   else:
     print("Valor depositado invalido.")


  elif opcao == "2":
    valor = float(input("\nInforme o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
      print("Impossivel realizar a operação, você não tem saldo suficiente!")

    elif excedeu_limite:
      print("Impossivel realizar a operação, você excedeu o limite de valor do saque!")

    elif excedeu_saques:
      print("Impossivel realizar a operação, você ultrapassou o limite de saques!")

    elif valor > 0:
      print(f"\nSeu saque de R$ {valor} foi realizado com sucesso!")
      saldo -= valor
      extrato += f"Saque: R$ {valor:.2f}\n"
      numero_saques += 1
      
    else:
     print("\nOperação falhou! Valor informado invalido")

  

  elif opcao == "3":
    print("\n============ Extrato ============")
    print("Não foi realizada nenhuma operação." if not extrato else extrato)
    print(f"\nSeu saldo é de: R${saldo:.2f}")
    print("\n=================================")

  
  elif opcao == "4":
    print("\n==============================================================")
    print("\nObrigado por utilizar nossos serviços, tenha um excelente dia!")
    print("\n==============================================================")
    break

  else:
    print("\nOperação inválida, por favor selecione novamente a operação desejada.")