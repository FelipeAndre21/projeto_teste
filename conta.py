import random
class Conta:

    def __init__(self, nome, sobrenome, saldo, senha, numero_conta):
        self.nome = nome
        self.sobrenome = sobrenome
        self.saldo = saldo
        self.senha = senha
        self.numero_conta = numero_conta

    def criar_conta():
        nome = str(input("nome: "))
        sobrenome = str(input("sobrenome: "))
        saldo = float(input("seu saldo: "))
        senha = int(input("sua senha: "))
        numero_conta = random.randint(100000,999999)
        print("Conta de {} {} possui saldo R$ {} seu numero da conta {}".format(nome, sobrenome, saldo, numero_conta))

    def validar_senha(self):
        pass

    def editar_conta(self):
        pass

    def deletar_conta(self):
        pass

    def mudar_saldo(self, valor):
        self.saldo = valor

    def sair(self):
        pass

