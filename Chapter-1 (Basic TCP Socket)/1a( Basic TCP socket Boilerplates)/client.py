import socket

#same as the server side
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=456

# here only clients wants to connect not wait
s.connect((host,port))

# rule: client talks and server responds
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

s.close() # closing
