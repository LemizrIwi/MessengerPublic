# server.py
import socket
import threading

HOST = '0.0.0.0'  # akzeptiert alle Verbindungen im Netzwerk
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            clients.remove(client)
            client.close()
            break

def receive():
    print(f"Server läuft auf {HOST}:{PORT}")
    while True:
        client, addr = server.accept()
        print(f"{addr} verbunden.")
        clients.append(client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
