from socket import *
from tkinter import *

import os
from _thread import *
ServerSideSocket = socket(AF_INET,SOCK_STREAM)
host = '127.0.0.1'
port = 2004
clients = []
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)

def recieving(conn):
    while True:
        msg = conn.recv(2048).decode('utf-8')
        
        for client in clients:
            if client != conn:
                client.send(msg.encode('utf-8'))
    

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    clients.append(Client)
    start_new_thread(recieving, (Client, ))

ServerSideSocket.close()