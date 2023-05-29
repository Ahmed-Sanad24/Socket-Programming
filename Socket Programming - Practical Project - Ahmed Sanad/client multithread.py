from socket import *
from tkinter import *
from tkinter import messagebox
import time

global state
state = 0

global flag
flag = False

global cnt1
cnt1 =0
global cnt2
cnt2 =0

ClientMultiSocket = socket(AF_INET,SOCK_STREAM)
host = '127.0.0.1'
port = 2004
print('Waiting for connection response')

def click1 ():
    global state
    lbl2.config(text=" 1 ")
    state = 1
def click2 ():
    global state
    lbl2.config(text=" 2 ")
    state = 2
def click3 ():
    global state
    lbl2.config(text=" 3 ")
    state = 3

def submits ():
    global state
    global flag
    global cnt1
    global cnt2

    if (state == 1):
        y = 1
        if (flag == False):
            ClientMultiSocket.connect((host, port))
            flag = True
        ClientMultiSocket.send(str(y).encode("utf-8"))
        res = ClientMultiSocket.recv(2048)
        result = res.decode('utf-8')
        if(result == str(y)):
            status.config(text="YOU WIN !")
            status2.config(text="YOU GUESSED : "+str(y))
            status3.config(text="HE CHOOSE : "+result)
            cnt1 += 1
            status4.config(text="SCORE =>             YOU : "+str(cnt1)+"   --   OTHER : "+str(cnt2))
        else:
            status.config(text="YOU LOSE !")
            status2.config(text="YOU GUESSED : "+str(y))
            status3.config(text="HE CHOOSE : "+result)
            cnt2 += 1
            status4.config(text="SCORE =>             YOU : "+str(cnt1)+"   --   OTHER : "+str(cnt2))
    elif (state == 2):
        y = 2
        if (flag == False):
            ClientMultiSocket.connect((host, port))
            flag = True        
        ClientMultiSocket.send(str(y).encode("utf-8"))
        res = ClientMultiSocket.recv(2048)
        result = res.decode('utf-8')
        if(result == str(y)):
            status.config(text="YOU WIN !")
            status2.config(text="YOU GUESSED : "+str(y))
            status3.config(text="HE CHOOSE : "+result)
            cnt1 += 1
            status4.config(text="SCORE =>             YOU : "+str(cnt1)+"   --   OTHER : "+str(cnt2))

        else:
            status.config(text="YOU LOSE !")
            status2.config(text="YOU GUESSED : "+str(y))
            status3.config(text="HE CHOOSE : "+result)
            cnt2 += 1
            status4.config(text="SCORE =>             YOU : "+str(cnt1)+"   --   OTHER : "+str(cnt2))

    elif (state == 3):
        y = 3
        if (flag == False):
            ClientMultiSocket.connect((host, port))
            flag = True        
        ClientMultiSocket.send(str(y).encode("utf-8"))
        res = ClientMultiSocket.recv(2048)
        result = res.decode('utf-8')
        if(result == str(y)):
            status.config(text="YOU WIN !")
            status2.config(text="YOU GUESSED : "+str(y))
            status3.config(text="HE CHOOSE : "+result)
            cnt1 += 1
            status4.config(text="SCORE =>             YOU : "+str(cnt1)+"   --   OTHER : "+str(cnt2))

        else:
            status.config(text="YOU LOSE !")
            status2.config(text="YOU GUESSED : "+str(y))
            status3.config(text="HE CHOOSE : "+result)
            cnt2 += 1
            status4.config(text="SCORE =>             YOU : "+str(cnt1)+"   --   OTHER : "+str(cnt2))

    else:
        messagebox.showerror("ERROR","Please Press on one of the 3 Buttons 1,2 or 3")


cw = Tk()
cw.title("Guess Game - Client 1 (Guesser)")
cw.geometry("400x300")

lbl1 = Label(cw, text="Guess The Number : ")
lbl1.grid(row=1,column=1,padx=5,pady=5)
lbl2 = Label(cw, text="")
lbl2.grid(row=1,column=2,padx=5,pady=5)

status = Label(cw,text="")
status.grid(row= 4, column=2,columnspan=3,pady=5)
status2 = Label(cw,text="")
status2.grid(row= 5, column=2,columnspan=3,pady=5)
status3 = Label(cw,text="")
status3.grid(row= 6, column=2,columnspan=3,pady=5)
status4 = Label(cw,text="")
status4.grid(row= 7, column=1,columnspan=6,pady=5)

btn1 = Button(cw , text="1",command=click1)
btn1.grid(row=2,column=2,padx=5,pady=5,ipadx=5)
btn2 = Button(cw , text="2", command=click2)
btn2.grid(row=2,column=3,padx=5,pady=5,ipadx=5)
btn3 = Button(cw , text="3",command=click3)
btn3.grid(row=2,column=4,padx=5,pady=5,ipadx=5)

submit= Button(cw,text="Guess",command=submits)
submit.grid(row=3 , column=2 ,columnspan=3,pady=15, ipadx= 10)





cw.mainloop()
