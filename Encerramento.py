while True:
    print("escreva [menu] para voltar ao menu principal")
    print("escreva [sair] para Sair")

    opcao = input("Escolha uma opção: ").lower()

    if opcao == 'menu':
        print("Voltando ao menu")
    elif opcao == 'sair':
        print("Encerrando o programa")
        break 
    else:
        print("Opção inválida, tente de novamente")