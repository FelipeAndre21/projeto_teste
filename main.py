from conta import Conta
from menu import Menu
from caixa_eletronico import Caixa_eletronico

print("Escolha a opção desejada: ")
opcao = int(input(
    "1 - cliente"
    "\n2 - gerente"
    "\n3 - sair: "
     "\nInforme a sua opção: "
                 ))
while True:

    if opcao == 1:
        Caixa_eletronico.criar_caixa_eletronico()
    elif opcao == 2:
        Menu.menu()
    elif opcao == 3:
        break
    else:
        print("opção invalida")
        break