from socket import * 
try:
    s=socket(AF_INET, SOCK_STREAM) 
    host="127.0.0.1"
    port=8002
    s.connect((host,port))
    while True:
        y=input("client : ") 
        s.send(y.encode('utf-8')) 
        x=s.recv(2048)
        print("server : ",x.decode('utf-8'))
    s.close()
except error as e: 
    print(e)
except KeyboardInterrupt : 
    print("chat is terminated")