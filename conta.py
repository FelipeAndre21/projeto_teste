import random
class Conta:

    def __init__(self, nome, sobrenome, saldo, senha, numero_conta):
        self.nome = nome
        self.sobrenome = sobrenome
        self.saldo = saldo
        self.senha = senha
        self.numero_conta = numero_conta

    def criar_conta():
        while True:
            nome = str(input("nome: ")).capitalize()
            sobrenome = str(input("sobrenome: ")).capitalize()
            saldo = float(input("seu saldo: "))
            senha = int(input("sua senha: "))
            numero_conta = random.randint(100000,999999)


            arquivo = open('gerentebd.txt', 'a')
            arquivo.write(
                "A conta  nome {} sobrenome {} saldo R$ {:.2f} senha {} conta {}\n".format(nome, sobrenome,saldo,
                                                                           senha, numero_conta))

            arquivo.close()

            arquivo = open('gerentebd.txt', 'r')
            for linha in arquivo:
                linha = linha.rstrip()
                print(linha)
            arquivo.close()
            break;
    def validar_senha(self):
        pass

    def editar_conta(self):
        pass

    def deletar_conta():

        arquivo = open('gerentebd.txt', 'r+')
        conta = int(input("digite numero da conta que deseja excluir:"))

        for linha in arquivo:
            linha = linha.rstrip()
            print(linha)
        arquivo.close()


    def mudar_saldo(saldo, valor):
        saldo = valor

    def sair(self):
        pass
