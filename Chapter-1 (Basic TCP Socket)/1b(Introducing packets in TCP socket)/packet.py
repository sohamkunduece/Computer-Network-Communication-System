import json

def create_packet(sender,receiver,message): # basic packet creating module
    packet={
        "header":"CHAT",
        "sender":sender,
        "reciver":receiver,
        "type":"TEXT",
        "length":len(message),
        "data":message
        }
    return json.dumps(packet)

def parse_packet(packet): # basic retriving data
    return json.loads(packet)
