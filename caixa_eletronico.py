from conta import Conta
class Caixa_eletronico(Conta):
    def __init__(self, numero_conta):
        super().__init__(numero_conta)
    def criar_caixa_eletronico():

        print("***Menu***")
        print("Escolha uma opção")

        opcao = int(input(
        "1 - depositar"
        "\n2 - sacar"
        "\n3 - transferir: "
         "\nInforme a sua opção: "
                     ))
        if opcao == 1:
            print("depositar")
            while True:
                valor = input("Qual valor que deseja depositar? ").replace(",", ".")
                try:
                    float(valor)
                except ValueError:
                    print("Valor digitado é invalido.")
                    continue
                break
            result = caixa.depositar(number, value)
            if not result:
                print("VALOR INVALIDO!")

            print("DEPOSOTADO COM SUCESSO, NOVO SALDO: {result['saldo']}")
            input("Pressione uma tecla para voltar ao menu anterior ")


        elif opcao == 2:
            def sacar(self, valor):
                self.saldo -= valor
        elif opcao == 3:
            def transferir(self, valor, destino):
                self.saca(valor)
                destino.deposita(valor)