def en_de(data,key):
    result=[]
    for i in range(len(data)):
        value=data[i]^key[i%len(key)]
        result.append(value)
    return bytes(result)