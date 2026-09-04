import socket as xp
import packet as sp
import threading as tp

s=xp.socket(xp.AF_INET,xp.SOCK_STREAM)
running=True

def receive():
    global running

    while running:
        # receive
        p = s.recv(1024).decode()

        if not p:
            print("Client disconnected.")
            running = False
            break

        data = sp.parse_packet(p)

        if data["data"].lower() == "exit":
            print("Server ended the chat.")
            running = False
            break

        print(f'\n{data["sender"]}: {data["data"]}')
        print("client :",end="",flush=True)


def send():
    global running

    while running:
        msg = input("client: ")

        p = sp.create_packet(
            sender="client",
            receiver="server",
            message=msg
        )

        s.send(p.encode())

        if msg.lower() == "exit":
            running = False
            break


host="127.0.0.1"
port=567
s.connect((host,port))

receive_thread = tp.Thread(target=receive, daemon=True)
send_thread = tp.Thread(target=send, daemon=True)

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()

s.close()
