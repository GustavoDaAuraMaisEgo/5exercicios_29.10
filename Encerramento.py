while True:
    print("[1] para voltar ao menu principal")
    print("[2] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("Voltando ao menu")
    elif opcao == '2':
        print("Encerrando o programa")
        break 
    else:
        print("Opção inválida, tente de novamente")