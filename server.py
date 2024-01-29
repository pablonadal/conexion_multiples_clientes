import socket, threading, asyncio, os

host = "127.0.0.1"
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()

clients = []
userNames = []
usersConnected = True

if not usersConnected:
    print("Server closed")
    os._exit(0)


def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)


def handle_messages(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            userName = userNames[index]
            broadcast(f"{userName} left the chat".encode("utf-8"), client)
            clients.remove(client)
            userNames.remove(userName)

            client.close()
            if index == 0:
                print("Server closed")
                global usersConnected
                usersConnected = False
            break


async def receive_connections():
    while True:
        client, address = await asyncio.to_thread(sock.accept)

        client.send("USER".encode("utf-8"))
        userName = (await asyncio.to_thread(client.recv, 1024)).decode("utf-8")

        clients.append(client)
        userNames.append(userName)

        print(f'User: {userName} connected with {str(address)}')

        message = f"{userName} joined the chat".encode("utf-8")
        broadcast(message, client)
        client.send("Connected to the server".encode("utf-8"))

        thread = threading.Thread(target=handle_messages, args=(client,))
        thread.start()

asyncio.run(receive_connections())
