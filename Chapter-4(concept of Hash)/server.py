import socket as xp
import packet as sp
import threading as tp
import logger
import hashlib


s = xp.socket(xp.AF_INET, xp.SOCK_STREAM)

running = True


def receive():
    global running

    while running:

        try:
            p = c.recv(4096).decode()

            if not p:
                print("Client disconnected.")
                running = False
                break

            data = sp.parse_packet(p)

            logger.log("receive", data["data"])


            # Hash verification
            calculated_hash = hashlib.sha256(
                data["data"].encode()
            ).hexdigest()


            if data["hash"].lower() != calculated_hash.lower():

                print("Channel compromised!!")
                logger.log("eavesdropping", "eve")


                msg = "exit"

                message_hash = hashlib.sha256(
                    msg.encode()
                ).hexdigest()


                p = sp.create_packet(
                    sender="server",
                    receiver="client",
                    message=msg,
                    hash_data=message_hash
                )


                c.send(p.encode())

                running = False
                break



            if data["data"].lower() == "exit":

                print("Client ended the chat.")
                logger.log("disconnect", "client side")

                running = False
                break



            print(f"\n{data['sender']}: {data['data']}")
            print("server:", end="", flush=True)


        except Exception as e:
            print("Receive error:", e)
            running = False



def send():

    global running


    while running:

        msg = input("server: ")


        message_hash = hashlib.sha256(
            msg.encode()
        ).hexdigest()



        p = sp.create_packet(
            sender="server",
            receiver="client",
            message=msg,
            hash_data=message_hash
        )


        c.send(p.encode())

        logger.log("sent", msg)


        if msg.lower() == "exit":

            running = False
            break




host = xp.gethostname()
port = 456


logger.log("server", "server started")


s.bind((host, port))
s.listen()


print("Waiting for client...")

c, addr = s.accept()


logger.log("connect", f"{addr} connected")

print("Got connection from", addr)



receive_thread = tp.Thread(
    target=receive,
    daemon=True
)


send_thread = tp.Thread(
    target=send,
    daemon=True
)


receive_thread.start()
send_thread.start()


receive_thread.join()
send_thread.join()


c.close()
s.close()
