import socket as xp
import threading as t

#it is noted no exception is handle. Key is 2 types of error will occur: connection and packet loss

host='0.0.0.0' # any prefered no but it is prefered to follow ip naming rule.
port=456

clients=[] #holds multiple client address

s=xp.socket(xp.AF_INET,xp.SOCK_STREAM)
s.bind((host,port))
s.listen()

def handle(conn,addr):
    print(f"connceted:{addr}")
    clients.append(conn)# save name of current joining client

    try:# this method is only to find which client left via exception handling
        while True:
            data=conn.recv(1024)
            if not data:
                break
            msg=data.decode()
            print(f"{addr}:{msg}")
            conn.send(data)#same message return
    except ConnectionError:
        pass
    finally:
        clients.remove(conn)
        conn.close()
        print(f"disconnected:{addr}")

#note: server is always on after work finish. to stop it for now you can just close manually or add exit context

while True: # this makes sure the part worksa s a thread and and when new connection open, fn is called
    conn,addr=s.accept()
    thread=t.Thread(
        target=handle,
        args=(conn,addr)
    )
    thread.start()