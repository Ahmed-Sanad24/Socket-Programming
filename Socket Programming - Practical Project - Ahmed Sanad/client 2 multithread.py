from socket import *
from tkinter import *
import time
from tkinter import messagebox


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


    

def starts():
    global check
    global flag
    global cnt1
    global cnt2
    if(enter.get()=='1' or enter.get()=='2' or enter.get()=='3'):
        if (flag == False):
            ClientMultiSocket.connect((host, port))
            flag = True
        res = ClientMultiSocket.recv(2048)
        result = res.decode('utf-8')


        if (enter.get() == result):
            y = enter.get()
            status.config(text="YOU LOSE !")
            ClientMultiSocket.send(y.encode('utf-8'))
            status2.config(text="HE GUESSED : "+result)
            status3.config(text="YOU CHOOSE : "+enter.get())
            cnt1 += 1
            status4.config(text="SCORE =>            YOU: "+str(cnt2)+"  --  OTHER: "+str(cnt1))

        else:
            y = enter.get()
            status.config(text="YOU WIN !")
            ClientMultiSocket.send(y.encode('utf-8'))
            status2.config(text="HE GUESSED : "+result)
            status3.config(text="YOU CHOOSE : "+enter.get())
            cnt2 += 1
            status4.config(text="SCORE =>            YOU: "+str(cnt2)+"  --  OTHER: "+str(cnt1))
    else:
        messagebox.showerror('ERROR',"Please Enter a Number Between 1 and 3")


    


    
    




cw = Tk()
cw.title("Guess Game - Client 2 (Chooser)")
cw.geometry("400x300")

lblname = Label(cw,text='Choose a Number : ')
lblname.grid(row=1,column=1,padx=5,pady=5)

enter = Entry(cw,)
enter.grid(row=1 , column=2,padx=5,pady=5)

waits = Label(cw,text="")
waits.grid(row= 3, column=2,columnspan=3)

status = Label(cw,text="")
status.grid(row= 4, column=2,columnspan=3,pady=5)
status2 = Label(cw,text="")
status2.grid(row= 5, column=2,columnspan=3,pady=5)
status3 = Label(cw,text="")
status3.grid(row= 6, column=2,columnspan=3,pady=5)
status4 = Label(cw,text="")
status4.grid(row= 7, column=1,columnspan=6,pady=5)




submit = Button(cw,text="Start",command=starts)
submit.grid(row=2,column=2, padx=5,pady=5, ipadx=15 )



#ClientMultiSocket.connect((host, port))
#res = ClientMultiSocket.recv(2048)
#result = res.decode('utf-8')

cw.mainloop()
