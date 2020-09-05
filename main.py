from src.caixa_eletronico import caixa_eletronico_main
from src.sistema_gerencia import *
from src.utils import write_menu


def main():
    while True:
        msg = "Digite qual sistema deseja Abrir: "
        options = (
                   (1, "Gerente"),
                   (2, "Cliente"),
                   (3, "Sair")
                   )

        selected_option = write_menu(options, msg)
        if selected_option == 3:
            break
        elif selected_option == 1:
            pass
        elif selected_option == 2:
            caixa_eletronico_main()





if __name__ == "__main__":
    main()
