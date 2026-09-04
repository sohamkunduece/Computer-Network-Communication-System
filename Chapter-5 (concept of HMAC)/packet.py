import json

def create_packet(sender, receiver, message,hash_data):
    packet = {
        "header": "CHAT",
        "sender": sender,
        "reciver": receiver,
        "type": "TEXT",
        "length": len(message),
        "data": message,
        "hash" :hash_data
    }
    return json.dumps(packet)

def parse_packet(packet):
    return json.loads(packet)
