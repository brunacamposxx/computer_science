import sys


if __name__ == "__main__":
    for argument in sys.argv:
        print("Received -> ", argument)

# Quando executamos um script e adicionamos parâmetros, os mesmos estarão disponíveis através de uma variável chamada sys.argv , que é preenchida sem que precisemos fazer nada.
