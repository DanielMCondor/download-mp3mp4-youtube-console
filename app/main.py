import platform, os
from download import download_mp3, download_mp4
from function import Color

SYSTEM = platform.system()
CLEAR = "cls" if SYSTEM.lower() == "windows" else "clear"
print(CLEAR)

OPC_MP3 = 1
OPC_MP4 = 2
OPC_SALIR = 0


def menu():
    return f""" Youtube - DanielMCondor
{OPC_MP3}) Descargar mp3
{OPC_MP4}) Descargar mp4
{OPC_SALIR}) Salir"""

def main():
    start = True
    while start:
        print(menu())
        option = input("Ingresa una opción: ")
        if is_option_invalid(option): continue
        option = int(option)
        if option == OPC_MP3:
            os.system(CLEAR)
            download_mp3()
        elif option == OPC_MP4:
            os.system(CLEAR)
            # download_mp4()
            Color.print_warning("mp4 aun esta en mantenimiento ...")
        elif option == OPC_SALIR:
            start = False
        else:
            Color.print_fail("Ingrese una opción válida ...")
        input("Presion enter para continuar ...")
        os.system(CLEAR)
    Color.print_ok("Gracias por tu visita ...")
    Color.print_info("Siempre me dara gusto verte ...")

# TODO: Validations
def is_option_invalid(option: str) -> bool:

    if not option.isnumeric():
        os.system(CLEAR)
        Color.print_fail("Ingrese una opción válida ...")
        input("Presiona enter para continuar ...")
        os.system(CLEAR)
        return True

    return False

# TODO: Excecute Main
if __name__ == "__main__":
    main()