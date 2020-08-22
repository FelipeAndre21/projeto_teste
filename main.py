import conta
print("******* MENU *******")
print("(1) criar conta - (2) editar conta - (3) deletar conta - (4) mudar saldo - (5) sair")
opcao = int(input("Escolha sua opção desejada: "))
if opcao == 1:
    print("criar conta")
    conta.Conta.criar_conta()
elif opcao ==2:
    print("editar conta")
elif opcao == 3:
    print("deletar conta")
elif opcao == 4:
    print("mudar saldo para {}".format(conta.Conta.mudar_saldo()))

elif opcao == 5:
    print("sair")
else:
    print("voce digitou opção inexistente")