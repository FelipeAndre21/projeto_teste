from conta import Conta


def white_menu(options):
    print("******* MENU *******")

    for op in options:
        print(f"{op[0]}:{op[1]}")

    while True:
        try:
            opcao = int(input("Escolha uma opção: \n "))
        except ValueError:
            print("voce digitou opção inexistente")
            continue
        if opcao in (1,2,3,4,5):
            return opcao


def caixa_eletronico(selected_option):
    if selected_option == 5:
        return False
    elif selected_option == 1:
        new_account = Conta()

        params = {
            "nome": "",
            "sobrenome": "",
            "senha": "",
            "saldo": ""
        }

        for data in params.keys():
            params[data] = input(f"Digite o {data}: ")

        new_account.criar_conta(params)
        return new_account

    elif selected_option == 2:
        cont = 3

        while True:
            if cont <= 0:
                return False
            number_account = input("Digite o numero da conta: ")
            conta = Conta(number_account)
            if not conta.is_valid():
                print("Conta inexistente no banco de dados...")
                print("Tente Novamente!")
                print(f"Quantidade restante de tentativas: {cont - 1}")
                cont -= 1
                continue
            cont = 3
            print(f"------ Seja Bem vindo(a)  {conta} --------------")
            break
        while True:
            print(cont)
            if cont < 3:
                print(f"Senha incorreta, entativas restantes de tentativas {cont - 1}")
            response = conta.consultar_saldo()
            if response['status_code'] == 200:
                for i in range(9):
                    print()
                print("-----------------------Saldo-----------------------")
                print(f"| Saldo: R$   {response.get('saldo')}                                            |")
                print("|                                                    |")
                print("|                                                    |")
                print("|                                                    |")

                print("-----------------------Fim Saldo---------------------|")
                for i in range(9):
                    print()
                break
            if cont == 0:
                print("Tentatias execedidas, tente mais tarde  ")
                break

            cont -=  1


def main():
    options = (
               (1, "Criar conta"),
               (2, "Consultar saldo"),
               (3, "deletar conta"),
               (4, "Mudar Saldo"),
               (5, "Sair")
               )

    selected_option = white_menu(options)

    caixa_eletronico(selected_option)



if __name__ == "__main__":
    main()
