from conta import Conta
from menu import Menu
from caixa_eletronico import Caixa_eletronico

while True:
    print("Escolha a opção desejada: ")
    opcao = int(input(
        "1 - cliente"
        "\n2 - gerente"
        "\n3 - sair: "
         "\nInforme a sua opção: "
                     ))


    if opcao == 1:
        Caixa_eletronico.criar_caixa_eletronico()
    elif opcao == 2:
        Menu.menu()
    elif opcao == 3:
        print("Obrigado por usar nosso sistema... Volte sempre :)")
        break
    else:
        print("*********")
        print("opção invalida")
        print("As opções são de 1 a 3 animal!!! ")
        print("*********")
        continue