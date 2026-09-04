import socket as xp
import packet as sp
import threading as tp
import logwithchannel as k

#function to send to client
def client_sent():
    global running

    while running:
        p=s_server.recv(1024).decode()
        data=sp.parse_packet(p)
        if (mode==2):
            k.log("server packet",data["data"])
        if(mode==3):
            data["data"]+=" (modified by eve)"
        p2=sp.create_packet(
            sender=data["sender"],
            receiver=data["reciver"],
            message=data["data"]
            )
        c.send(p2.encode())
        if data["data"].lower()=="exit":
            running=False
            break

#function to send to server
def server_sent():
    global running

    while running:
        p=c.recv(1024).decode()
        data=sp.parse_packet(p)
        if (mode==2):
            k.log("client packet",data["data"])
        if(mode==3):
            data["data"]+=" (modified by eve)"
        p2=sp.create_packet(
            sender=data["sender"],
            receiver=data["reciver"],
            message=data["data"]
            )
        s_server.send(p2.encode())
        if data["data"].lower()=="exit":
            running=False
            break

        
#mode creation
print("TYPE of channel")
print("Mode 1 no evesdropping")
print("Mode 2 passive evesdropping")
print("Mode 3 active evesdropping")
while True:
    mode=int(input("Choose mode:"))
    if (mode==1 or mode==2 or mode==3):
        break
    print("wrong choice!! try again.")

#socket creation
s_server=xp.socket(xp.AF_INET,xp.SOCK_STREAM)
s_client=xp.socket(xp.AF_INET,xp.SOCK_STREAM)

#global variable
running=True

#IP and port defination
host_server = xp.gethostname()
host_client="127.0.0.1"
port_server = 456
port_client=567

#connection to server
if not(s_server.connect((host_server,port_server))):
    print("connected to server")

#connection from client
s_client.bind((host_client,port_client))
s_client.listen()
c,addr=s_client.accept()
print("Got connection from", addr)

#threads
recieve_thread=tp.Thread(target=server_sent, daemon=True)
sent_thread=tp.Thread(target=client_sent, daemon=True)
recieve_thread.start()
sent_thread.start()
recieve_thread.join()
sent_thread.join()

#closing
c.close()
s_client.close()
s_server.close()
