from conta import Conta
print("******* MENU *******")
print("(1) criar conta - (2) editar conta - (3) deletar conta - (4) mudar saldo - (5) sair")
opcao = 1
while opcao == 1 or 2 or 3 or 4 or 5:
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        print("criar conta")
        Conta.criar_conta()
    elif opcao == 2:
        print("editar conta")
    elif opcao == 3:
        print("deletar conta")
    elif opcao == 4:
        print("mudar saldo para")
        saldo = float(input("Novo saldo: "))

    elif opcao == 5:
        print("sair")
        break
else:
    print("voce digitou opção inexistente")