# main.py

import justpy as jp
from interface.cadastro_view import pagina_cadastro


def main():
    print("Iniciando servidor web...")
    print("Abra no navegador: http://127.0.0.1:8000")

    jp.justpy(pagina_cadastro)


if __name__ == "__main__":
    main()