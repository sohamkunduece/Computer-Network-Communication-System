import socket as sp

host="127.0.0.1" #or you can use gethost feature. note it better to use the give host adress for server0.0.0.0 and client 127.0.0.1 to prevent issues
port=808 

s=sp.socket(sp.AF_INET,sp.SOCK_DGRAM)

#first send,dont connect
message="Hello from client"

s.sendto(message.encode(),(host,port))

data,server_adr=s.recvfrom(1024)#1024 is buffer size
message=data.decode()
print(f"received from {server_adr}:{message}")

