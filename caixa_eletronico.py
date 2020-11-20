class Caixa_eletronico:
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

            def depositar(self, valor):
                self.saldo += valor
        elif opcao == 2:
            def sacar(self, valor):
                self.saldo -= valor
        elif opcao == 3:
            def transferir(self, valor, destino):
                self.saca(valor)
                destino.deposita(valor)