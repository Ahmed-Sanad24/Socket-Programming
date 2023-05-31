import tkinter as tk
import socket
import threading
from time import sleep
from tkinter import messagebox


window = tk.Tk()
window.title("Server main window")
window.geometry("300x320+0+0")
window.configure(bg="#838996")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

firstframe = tk.Frame(window)
lbl_author = tk.Label(firstframe,pady=5,bg="#50C878",text="Author : Ahmed Sanad Ibrahim")
lbl_author.pack( side=tk.TOP)
firstframe.grid(row=0)
# Top frame consisting of two buttons widgets (i.e. btnStart, btnStop)
topFrame = tk.Frame(window)
topFrame.grid(row=1, column=0)


btnStart = tk.Button(topFrame, text="Start", padx=20, command=lambda: start_server())
btnStart.grid(row=0, column=0)


btnStop = tk.Button(topFrame, text="Stop", padx=20, command=lambda: stop_server())
btnStop.grid(row=0, column=1)


#  displaying the host and port info

lblHost = tk.Label(topFrame, text="Address:    (Not Set)")
lblHost.grid(row=1, column=0, columnspan=2, sticky="w")
lblPort = tk.Label(topFrame, text="Port:     (Not Set)")
lblPort.grid(row=2, column=0, columnspan=2, sticky="w")

# The client frame shows the client area
clientFrame = tk.Frame(window,bg="#838996")
lbllisten = tk.Label(clientFrame, text="",bg="#838996")
lbllisten.pack(side=tk.TOP)
lblLine = tk.Label(clientFrame, text="============= Player Names =============").pack()
scrollBar = tk.Scrollbar(clientFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(clientFrame, height=10, width=30)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(
    yscrollcommand=scrollBar.set,
    background="black",
    highlightbackground="grey",
    state="disabled",

)
clientFrame.grid(row=3, column=0, columnspan=2, pady=(5, 10))


server = None
HOST_ADDR = "127.0.0.1"
HOST_PORT = 12345
client_name = " "
clients = []
clients_names = []
clients_ips = []  # Store the IP addresses of the clients
player_data = []


# Start server function
def start_server():
    global server, HOST_ADDR, HOST_PORT  # code is fine without this
    btnStart.config(state=tk.DISABLED,bg="#50C878",fg='white')
    btnStop.config(state=tk.NORMAL)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server is listening on port: " + str(HOST_PORT))

    server.bind((HOST_ADDR, HOST_PORT))
    server.listen(2)  # server is listening for client connection
    lbllisten.config(text="server is listening for client connection ...",fg="green")

    print("Server started. Waiting for connections...")

    threading._start_new_thread(accept_clients, (server, " "))

    lblHost["text"] = "Address: " + HOST_ADDR
    lblPort["text"] = "Port: " + str(HOST_PORT)


# Stop server function
def stop_server():
    global server
    server.close()
    btnStart.config(state=tk.NORMAL)
    btnStop.config(state=tk.DISABLED)


def accept_clients(the_server, y):
    while True:
        player1_socket, player1_address = the_server.accept()
        clients.append(player1_socket)
        print("Player 1 connected.")
        player1_socket.send("guesser".encode())
        sleep(0.5)
        threading._start_new_thread(send_receive_client_message, (player1_socket, player1_address))

        player2_socket, player2_address = the_server.accept()
        clients.append(player2_socket)
        print("Player 2 connected.")
        player2_socket.send("chooser".encode())
        sleep(0.5)
        threading._start_new_thread(send_receive_client_message, (player2_socket, player2_address))


# Function to receive message from current client AND
# Send that message to other clients
def send_receive_client_message(client_connection, client_ip_addr):
    global server, client_name, clients, player_data, player0, player1

    client_msg = " "

    # send welcome message to client
    client_name = client_connection.recv(4096).decode()

    if len(clients) < 2:
        client_connection.send("welcome1".encode())
    else:
        client_connection.send("welcome2".encode())

    clients_names.append(client_name)
    clients_ips.append(client_ip_addr[0])  # Store the client's IP address
    update_client_names_display(clients_names, clients_ips)  # update client names display

    if len(clients) > 1:
        sleep(1)

        # send opponent name
        clients[0].send(("opponent_name$" + clients_names[1]).encode())
        clients[1].send(("opponent_name$" + clients_names[0]).encode())
        # go to sleep

    while True:
        data = client_connection.recv(4096).decode()
        print(data)
        if not data:
            break

        # get the player choice from received data
        player_choice = data[11: len(data)]

        msg = {"choice": player_choice, "socket": client_connection}

        if len(player_data) < 2:
            player_data.append(msg)

        if len(player_data) == 2:
            # send player 1 choice to player 2 and vice versa
            dataToSend0 = "$opponent_choice" + player_data[1].get("choice")
            dataToSend1 = "$opponent_choice" + player_data[0].get("choice")
            player_data[0].get("socket").send(dataToSend0.encode())
            player_data[1].get("socket").send(dataToSend1.encode())

            player_data = []


# Update client name display when a new client connects OR
# When a connected client disconnects
def update_client_names_display(name_list, ip_list):
    tkDisplay.config(state=tk.NORMAL)
    tkDisplay.delete("1.0", tk.END)

    for name, ip in zip(name_list, ip_list):
        tkDisplay.insert(tk.END, f"{name} ({ip})\n")
    tkDisplay.config(state=tk.DISABLED)


window.mainloop()
