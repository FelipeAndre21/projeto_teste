from .conta import Conta
from .utils import write_menu
import os


class CaixaEletronica(Conta):
    def __init__(self, numero_conta):
        super().__init__(numero_conta)

    def write_saldo(self, saldo):
        """25 de largura"""
      #
        top = " " * 12 + "*" * 10 + "saldo" + "*" * 10 + " " * 12
        value = " " * 12 + "| Saldo : R$ " + saldo + " " * (25 - len(saldo) - 14) + "|"  + " " * 12
        mind = " " * 12 + "|" + " " * 23 + "|"
        down = " " * 12 + "*" * 10 + " Fim " + "*" * 10 + " " * 12
        print("| hiufhhgf |")
        print()
        print()
        print(top)
        print(value)
        print(mind)
        print(mind)
        print(down)

def caixa_eletronico_main():
    status = None
    while True:
        options = (
            (1, "Consultar Saldo"),
            (2, "Fazer Deposito"),
            (3, "Sair")
        )
        if not status:
            number = input("Digite o numero da sua conta : \n")
            caixa = CaixaEletronica(number)
        msg = f"Bem Vindo {caixa} ao Sitema de caixa eletronico \n" \
              "Digite a opção desejada : "
        selected_option = write_menu(options, msg)
        if selected_option == 3:
            return False
        elif selected_option == 1:
            count = 0
            while True:
                if count > 0:
                    print("Senha incorreta, digite novamente")
                    print(f"quantidade restante de tentativas: {3 - count}")
                status, saldo = caixa.consultar_saldo()
                if status:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    caixa.write_saldo(saldo)
                    input("Pressione Uma tecla para voltar ao menu anterior")
                    break
                if count >= 3:
                    break
                count += 1

        elif selected_option == 2:
            while True:
                value = input("Qual valor que deseja depositar? ").replace(",", ".")
                try:
                    float(value)
                except ValueError:
                    print("Valor digitado é invalido.")
                    continue
                break
            result = caixa.depositar(number, value)
            if not result:
                print("VALOR INVALIDO!")
                continue
            print(f"DEPOSOTADO COM SUCESSO, NOVO SALDO: {result['saldo']}")
            input("Pressione uma tecla para voltar ao menu anterior ")
            break