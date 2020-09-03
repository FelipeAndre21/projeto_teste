import random
from lib.auth import Authenticator
class Decorator(object):
    def __init__(self,decoratee_enclosing_class):
        self.decoratee_enclosing_class = decoratee_enclosing_class

    def __call__(self,original_func):
        def get_password_save(*args, **kwargs):
            password = input("Digite a sua senha: ")
            if str(args[0].get_password()) == password:
                return original_func(*args, **kwargs)
            return acesso_negado()

        return get_password_save
def acesso_negado():
    print("Senha incorreto")
# def check_password(func):
#     def get_password_save(*args, **kwargs):
#         print()
#         # senha = self.get_attr("senha")
#         pass
#
#     a = get_password_save()
#     return func
#     # password = input("Digite sua senha: ")
    # senha = self.get_attr("senha")
    # if str(password) == str(senha):
    #     return func
    # return self.acesso_negado
class Conta:
    def __init__(self, number_account=None):
        self._data = self.get_attr(number_account)
        self._number_account = number_account

    def get_password(self):
        return self._data['senha']

    def is_valid(self):
        if self._data:
            return True
        return False
    # def criar_conta(self, params):
    #
    #
    #     params['numero_conta'] = random.randint(000000, 999999)
    #
    #     file = open(f"contas/{params['numero_conta']}.txt", "w")
    #     for key, value in params.items():
    #         file.write(
    #             "{0}:{1} \n".format(str(key), str(value))
    #         )
    @Authenticator("Conta")
    def consultar_saldo(self):
        return {
               "status_code": 200,
               "message": f"Seu saldo atual é : {self._data.get('saldo')}," \
                          f" sujeito a alteração até o fim do dia",
               "saldo": self._data.get("saldo")

       }

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

    def sair(self):
        pass

    def __str__(self):
        return self._data['nome']

