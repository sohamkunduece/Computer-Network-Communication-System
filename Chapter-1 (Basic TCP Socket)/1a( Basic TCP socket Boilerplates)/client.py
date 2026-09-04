import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=456

s.connect((host,port))

while True:
    #recieve
    msg= s.recv(1024).decode()
    if not msg: # Add this!
        print("Server disconnected.")
        break
    

    if msg.lower()=="exit":
                print("server ended the chat")
                break

    print("server:",msg)

    #reply
    msg=input("client: ")
    
    s.send(msg.encode())

    if msg.lower()=="exit":
        break

s.close()
