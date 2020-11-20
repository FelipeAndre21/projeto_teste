from conta import Conta
class Menu:
    def menu():

        opcao = 1
        while opcao == 1 or 2 or 3 or 4:
            print("******* MENU *******")
            print("(1) criar conta - (2) editar conta - (3) deletar conta - (4) sair")
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                    print("criar conta")
                    Conta.criar_conta()
            elif opcao == 2:
                    print("editar conta")
                    Conta.editar_conta()
            elif opcao == 3:
                    print("deletar conta")
                    Conta.deletar_conta()
            elif opcao == 4:
                    print("sair")
                    break
            else:
                        print("voce digitou opção inexistente")


