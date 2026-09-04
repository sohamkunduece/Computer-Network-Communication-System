import socket as xp

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
c.send(msg.encode())

while True:
   #recieve
    msg = c.recv(1024).decode()
    if not msg: # Add this!
        print("Client disconnected.")
        break
    

    if msg.lower()=="exit":
                print("client ended the chat")
                break

    print("client:",msg)

    #reply
    msg=input("server: ")

    c.send(msg.encode())

    if msg.lower()=="exit":
        break

    
c.close()
s.close()
