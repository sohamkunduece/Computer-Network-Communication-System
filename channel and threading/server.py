import socket as xp
import packet as sp
import threading as tp
import logger

s = xp.socket(xp.AF_INET, xp.SOCK_STREAM)

running = True   # Shared flag


def receive():
    global running

    while running:
        # receive
        p = c.recv(1024).decode()

        if not p:
            print("Client disconnected.")
            running = False
            break

        data = sp.parse_packet(p)
        logger.log("recieve",data["data"])

        if data["data"].lower() == "exit":
            print("Client ended the chat.")
            logger.log("disconnect","client side")
            running = False
            break

        print(f'\n{data["sender"]}: {data["data"]}')
        print("server:",end="",flush=True)


def send():
    global running

    while running:
        msg = input("server: ")
        logger.log("sent",msg)

        p = sp.create_packet(
            sender="server",
            receiver="client",
            message=msg
        )

        c.send(p.encode())
        logger.log("disconnect","server side")

        if msg.lower() == "exit":
            running = False
            break


host = xp.gethostname()
port = 456
logger.log("server","server started")

s.bind((host, port))
s.listen()

c, addr = s.accept()
logger.log("connect",f"{addr} connected")
print("Got connection from", addr)


receive_thread = tp.Thread(target=receive, daemon=True)
send_thread = tp.Thread(target=send, daemon=True)

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()

c.close()
s.close()
