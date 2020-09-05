import os


def write_menu(options, msg=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    number_options =[]
    print("******************************** MENU ***************************************")
    if msg:
        print(msg)
    for op in options:
        print(f"{op[0]}:{op[1]}")
        number_options.append(op[0])

    while True:
        try:
            opcao = int(input("Escolha uma opção: \n "))
        except ValueError:
            print("voce digitou opção inexistente")
            continue

        if opcao in number_options:
            return opcao
        print("Numero não corresponde a nenhuma opção, tente novamente")

# def convert_to_real(value):
#     """12.000,90"""
#     number = str(int(float(value.replace(".","").replace(",","."))))
#     count = 1
#     for i in range(int(len(number)/3)):
#         converted = number[:3] +"."+ number[3:]
#         count += 1
#     print(converted)



# if __name__ == "__main__":
#     options = (
#
#         (1, "Gerente"),
#
#         (3, "Sair")
#     )
#     msg = "Diite qual sistema deseja abrir?"
#     white_menu(options, msg)