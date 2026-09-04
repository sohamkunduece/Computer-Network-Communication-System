import socket as xp
import packet as sp
import threading as tp
import logwithchannel as k
import json


# Function to forward server -> client
def client_sent():
    global running

    while running:

        p = s_server.recv(1024).decode()

        if not p:
            running = False
            break

        data = sp.parse_packet(p)

        # Passive Eve
        if mode == 2:
            k.log("server packet", data["data"])

        # Active Eve
        elif mode == 3:
            data["data"] += " (modified by eve)"
            data["length"] = len(data["data"])

        # Forward packet
        p2 = json.dumps(data)
        c.send(p2.encode())

        if data["data"].lower().startswith("exit"):
            running = False
            break


# Function to forward client -> server
def server_sent():
    global running

    while running:

        p = c.recv(1024).decode()

        if not p:
            running = False
            break

        data = sp.parse_packet(p)

        # Passive Eve
        if mode == 2:
            k.log("client packet", data["data"])

        # Active Eve
        elif mode == 3:
            data["data"] += " (modified by eve)"
            data["length"] = len(data["data"])

        # Forward packet
        p2 = json.dumps(data)
        s_server.send(p2.encode())

        if data["data"].lower().startswith("exit"):
            running = False
            break


# ------------------ Mode Selection ------------------

print("TYPE of channel")
print("Mode 1 : No eavesdropping")
print("Mode 2 : Passive eavesdropping")
print("Mode 3 : Active eavesdropping")

while True:

    mode = int(input("Choose mode : "))

    if mode in [1, 2, 3]:
        break

    print("Wrong choice! Try again.")


# ---------------- Socket Creation ----------------

s_server = xp.socket(xp.AF_INET, xp.SOCK_STREAM)
s_client = xp.socket(xp.AF_INET, xp.SOCK_STREAM)

running = True

host_server = xp.gethostname()
host_client = "127.0.0.1"

port_server = 456
port_client = 567


# Connect to Bob(Server)
s_server.connect((host_server, port_server))
print("Connected to server")


# Wait for Alice(Client)
s_client.bind((host_client, port_client))
s_client.listen()

c, addr = s_client.accept()
print("Got connection from", addr)


# ---------------- Threads ----------------

receive_thread = tp.Thread(target=server_sent, daemon=True)
send_thread = tp.Thread(target=client_sent, daemon=True)

receive_thread.start()
send_thread.start()

receive_thread.join()
send_thread.join()


# ---------------- Closing ----------------

c.close()
s_client.close()
s_server.close()
