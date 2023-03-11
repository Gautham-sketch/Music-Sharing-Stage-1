import socket
from threading import Thread

SERVER = None
IP_ADDRESS = '127.0.0.1'
PORT = 8050
bufferSize = 4096
clients = {}

def acceptConnections():
    global SERVER
    global clients

    while True:
        client, addr = SERVER.accept()
        print(client, addr)

def setup():
    print("\n\t\t\t\t\t\tIP MESSENGER\n")

    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))

    SERVER.listen()

    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS......")
    print("\n")

    acceptConnections()


setup_thread = Thread(target=setup)
setup_thread.start()