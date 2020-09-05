import random
from lib.auth import Authenticator

class Conta:
    def __init__(self, number_account=None):
        self._data = self.get_attr(number_account)
        self._number_account = number_account

    def get_password(self):
        return self._data['senha']

    def __criar_account(self):
        params = {
                "nome": "",
                "sobrenome": "",
                "senha": "",
                "saldo": ""
            }

        for data in params.keys():
            params[data] = input(f"Digite o {data}: ")
        while True:
            params['numero_conta'] = random.randint(000000, 999999)
            if not self.account_exists(params['numero_conta']):
                break
        self.insert_data_account(params)

        return True, params

    @staticmethod
    def account_exists(number_account):
        try:
            file_open = open(f"contas/{number_account}")
        except FileNotFoundError:
            return False
        file_open.close()
        return True

    @Authenticator("Conta")
    def consultar_saldo(self):
        return True, self._data['saldo']

    def insert_data_account(self, params, account_number):
        file = open(f"contas/{account_number}.txt", "w")
        for key, value in params.items():
            file.write(
                "{0}:{1} \n".format(str(key), str(value))
            )
        file.close()

    @Authenticator("Conta")
    def depositar(self, number_account, value):
        if float(value) > 0:
            data = self.get_attr(number_account)
            new_saldo = str(
                float(data['saldo'].replace(",",".")) + float(value)
            ).replace(".",",")
            data['saldo'] = new_saldo
            self.insert_data_account(data, number_account)
            return data
        return False


    def get_attr(self, number_account):
        data = {}
        file = None
        try:
            file = open(f"contas/{number_account}.txt", "r")
        except Exception as err:
            return False


        for i in file:
            data[i.split(":")[0]] = i.split(":")[1].replace("\n", "").replace(" ","")

        return data


    def __str__(self):
        return self._data['nome']

