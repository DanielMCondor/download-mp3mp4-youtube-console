from download import download_mp3, download_mp4
from function import Print, Clear

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
        Print.banner()
        print(menu())

        option = input("Ingresa una opción: ")
        if is_option_invalid(option): continue
        option = int(option)
        if option == OPC_MP3:
            Clear()
            download_mp3()
        elif option == OPC_MP4:
            Clear()
            download_mp4()
        elif option == OPC_SALIR:
            start = False
        else:
            Print.fail("Ingrese una opción válida ...")
        input("Presion enter para continuar ...")
        Clear()
    Print.banner()
    Print.ok("Gracias por tu visita ...")
    Print.info("Siempre me dara gusto verte ...")

# TODO: Validations
def is_option_invalid(option: str) -> bool:

    if not option.isnumeric():
        Clear()
        Print.fail("Ingrese una opción válida ...")
        input("Presiona enter para continuar ...")
        Clear()
        return True

    return False

# TODO: Excecute Main
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        Print.fail("-> Cerraste la aplicación a la fuerza ...")