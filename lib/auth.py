class Authenticator:
    def __init__(self, decorate_enclosing_class):
        self.decorate_enclosing_class = decorate_enclosing_class

    def __call__(self, original_func):
        def get_password_save(*args, **kwargs):
            password = input("Digite a sua senha: ")
            if str(args[0].get_password()) == str(password):
                return original_func(*args, **kwargs)
            input("Acesso negado!")
            return False, self._access_denied()

        return get_password_save

    @staticmethod
    def _access_denied():
        return {
            "status_code": 403,
            "message": "access_denied"
        }

def teste(n,b, op):
    def soma():
        return n + b
    if op.upper() == "SOMA":
        return soma()
    return True