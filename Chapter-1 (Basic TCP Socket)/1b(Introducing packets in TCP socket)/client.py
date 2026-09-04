import socket
import packet as sp

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=456

s.connect((host,port))

while True:
    #recieve
    p = s.recv(1024).decode()
    if not p: # Add this!
        print("Server disconnected.")
        break
    data = sp.parse_packet(p)

    if data["data"].lower()=="exit":
                print("server ended the chat")
                break

    print(f'{data["sender"]}:{data["data"]}')

    #reply
    msg=input("client: ")
    p=sp.create_packet(
        sender="client",
        receiver="server",
        message=msg
        )
    s.send(p.encode())

    if msg.lower()=="exit":
        break

s.close()
