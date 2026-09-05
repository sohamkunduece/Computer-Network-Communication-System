import socket as xp

#AF_iNET uses ipv4 address for ipv6 use AF_INET6 AF_UNIX uuse in sma ecomputer and od not use ip address
# SOCK_STREAM like telephone(TCP) and Sock_DGRAM uses UDP
# for UDP boiler plate go to appendix 2
s=xp.socket(xp.AF_INET,xp.SOCK_STREAM)

host=xp.gethostname() #host and port no is like an address and house no without it we dont knowwhere to connect.
port=456 #Dont worry, application genrally have fixed address and house no

s.bind((host,port)) #fixes the address

s.listen()# waiting for if anyone asking for connection. genrally, listen has timer but for study purpose we removed it

c,addr=s.accept() #if a client wantsto communicat server accepts it. Note the system is for one client. for multiple client go to appendix 1
print('Got connection from ',addr)
msg="Thank you for connected. Ready to recieve message!please type \"exit\" to end"
c.send(msg.encode()) # data can be send via bits, as computer only understand 1,0

while True:# the setup is server listens and then reply
   #recieve
    msg = c.recv(1024).decode()
    if not msg: # Add this if not for message. sometimes it happens due to internal problems or device. dont panic.
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

    
c.close() # closing communication
s.close()
