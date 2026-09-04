import json

def create_packet(sender,receiver,message):
    packet={
        "header":"CHAT",
        "sender":sender,
        "reciver":receiver,
        "type":"TEXT",
        "length":len(message),
        "data":message
        }
    return json.dumps(packet)

def parse_packet(packet):
    return json.loads(packet)
