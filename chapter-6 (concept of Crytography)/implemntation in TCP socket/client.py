import socket as xp
import packet as sp
import threading as tp
import hmac
import logger
import hashlib
import diy_encrytion as d

s = xp.socket(
    xp.AF_INET,
    xp.SOCK_STREAM
)


running = True

SECRET_KEY = b"my_secret_key"
encrypt_key= b"hello"

def receive():

    global running


    while running:

        try:

            p = s.recv(4096).decode()


            if not p:

                print("Server disconnected.")

                running=False
                break



            data = sp.parse_packet(p)


            logger.log(
                "receive",
                data["data"]
            )


            calculated_hash = hmac.new(
                SECRET_KEY,
                data["data"],
                hashlib.sha256
            ).hexdigest()



            if data["hash"].lower() != calculated_hash.lower():

                print("Channel compromised!!")

                msg="exit"


                message_hash = hashlib.sha256(
                    msg
                ).hexdigest()



                p = sp.create_packet(
                    sender="client",
                    receiver="server",
                    message=msg,
                    hash_data=message_hash
                )


                s.send(p.encode())


                running=False
                break

            msg=data["data"]
            msg=d.en_de(msg,encrypt_key)
            msg=int.from_bytes(msg)


            if msg.lower()=="exit":

                print("Server ended the chat.")

                running=False
                break



            print(
                f"\n{data['sender']}: {data['data']}"
            )

            print("client:", end="", flush=True)



        except Exception as e:

            print("Receive error:",e)

            running=False




def send():

    global running


    while running:


        msg=input("client: ")
        msg = input("server: ")
        msg=int.to_bytes(msg)
        msg=d.en_de(msg,encrypt_key) #encryption done here


        message_hash = hmac.new(
            SECRET_KEY,
            msg,
            hashlib.sha256
        ).hexdigest()



        p = sp.create_packet(
            sender="client",
            receiver="server",
            message=msg,
            hash_data=message_hash
        )



        s.send(p.encode())


        logger.log(
            "sent",
            msg
        )



        if msg.lower()=="exit":

            running=False
            break





host="127.0.0.1"
port=567


s.connect(
    (host,port)
)


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


s.close()
