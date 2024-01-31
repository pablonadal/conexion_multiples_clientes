import socket, threading
from main import main
from time import sleep
from constants import *
from filter import censor_insults

def run_client(userName):
    host = "127.0.0.1"
    port = 8080

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
    except socket.error as e:
        print("No se pudo conectar al servidor. \nVolviendo al menú principal.")
        sleep(2)
        return False

    def receive_messages():
        while True:
            try:
                receivedMessage = client.recv(1024).decode("utf-8")
                if receivedMessage == "USER":
                    client.send(userName.encode("utf-8"))
                else:
                    print(f"\n{receivedMessage}\n")
            except:
                print("An error ocurred!")
                main()
                client.close()
                break

    def write_messages():
        while True:
            writedMessage = censor_insults(input(""))
            if writedMessage == "close":
                client.close()
                break
            else:
                client.send((f"{userName}: {writedMessage}").encode("utf-8"))
    
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    write_thread = threading.Thread(target=write_messages)
    write_thread.start()

    return True
