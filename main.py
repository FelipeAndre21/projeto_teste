from conta import Conta
from menu import Menu

print("Escolha a opção desejada: ")
opcao = int(input(
    "1 - cliente"
    "\n2 - gerente"
    "\n3 - sair: "
     "\nInforme a sua opção: "
                 ))
while True:

    if opcao == 1:
        pass
    elif opcao == 2:
        Menu.menu()
    elif opcao == 3:
        break
    else:
        print("opção invalida")
        break