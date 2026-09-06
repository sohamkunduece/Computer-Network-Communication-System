import socket as sp

host="0.0.0.0" #or you can use gethost feature(note check if the ip address is allocated to your device)
port=808 

s=sp.socket(sp.AF_INET,sp.SOCK_DGRAM)
s.bind((host,port))

while True:
    data,client_adr=s.recvfrom(1024)#1024 is buffer size
    message=data.decode()
    print(f"received from {client_adr}:{message}")

    response="Hello from server"
    s.sendto(response.encode(),client_adr)