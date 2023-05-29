from socket import * 
try:
    s=socket(AF_INET, SOCK_STREAM) 
    host="127.0.0.1"
    port=8002
    s.bind((host,port))
    s.listen(5)
    client, addr=s.accept() 
    print("connection from", addr[0]) 
    while True:
        x=client.recv(2048)
        print("client : ",x.decode('utf-8'))
        y=input(" server : ") 
        client.send(y.encode('utf-8'))
    s.close()
except error as e:
    print(e)
except KeyboardInterrupt :
    print("chat is terminated")