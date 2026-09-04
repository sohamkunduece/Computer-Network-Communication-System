import diy_encrytion as d

#sending side
message=b"hello" #for encryption we should focus on binary
key=b"steve"

encryption=d.en_de(message,key) #ciphertext creation
print(encryption)

decrypt=d.en_de(encryption,key)
print(decrypt)