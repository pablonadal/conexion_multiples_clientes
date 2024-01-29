from time import sleep
from constants import *
from client import *

def main():
    clear_screen()

    while True:
        display_menu()

        choice = input("Opción: ")

        if choice == "1":
            clear_screen()
            run_server()
            if not run_client(get_user_name()):
                continue
            break
        elif choice == "2":
            clear_screen()
            if not run_client(get_user_name()):
                continue
            break
        elif choice == "3":
            exit_program()
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

def get_user_name():
    return input("Hola, ingresa tu nombre para continuar: ")


def display_menu():
    menu = (
        f"\nPor favor, selecciona una opción."
        "\n================================="
        "\n1. Crear sala de chat"
        "\n2. Unirse a sala de chat"
        f"\n3. Salir"
        "\n================================="
    )
    print(menu)

def exit_program():
    clear_screen()
    sleep(1)
    print("¡Hasta luego!")
    sleep(1)

if __name__ == "__main__":
    main()
