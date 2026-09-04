import socket as xp
import packet as sp

#AF_iNET uses ipv4 address for ipv6 use AF_INET6 AF_UNIX uuse in sma ecomputer and od not use ip address
# SOCK_STREAM like telephone(TCP) and Sock_DGRAM uses UDP
s=xp.socket(xp.AF_INET,xp.SOCK_STREAM)

host=xp.gethostname()
port=456

s.bind((host,port))

s.listen()

c,addr=s.accept()
print('Got connection from ',addr)
msg="Thank you for connected. Ready to recieve message!please type \"exit\" to end"
p=sp.create_packet(
        sender="server",
        receiver="client",
        message=msg
        )
c.send(p.encode())

while True:
   #recieve
    p = c.recv(1024).decode()
    if not p: # Add this!
        print("Client disconnected.")
        break
    data = sp.parse_packet(p)

    if data["data"].lower()=="exit":
                print("client ended the chat")
                break

    print(f'{data["sender"]}:{data["data"]}')

    #reply
    msg=input("server: ")
    p=sp.create_packet(
        sender="server",
        receiver="client",
        message=msg
        )
    c.send(p.encode())

    if msg.lower()=="exit":
        break

    
c.close()
s.close()
