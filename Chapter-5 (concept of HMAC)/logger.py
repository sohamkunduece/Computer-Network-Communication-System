from datetime import datetime

def log(event,details):
    time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat.log","a") as file:
        file.write(f"[{time}]{event}:{details}\n")
