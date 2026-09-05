Chapter-1b

Application- Setup a basic Communication system (part-2).

Objective:
1.creation of packet for data transfer.

Theory:
Data cannot be transfer together all at once. The reason is each data is of 100s of bits. Moreover while sending data alone, important important information like "is data being corrupeted while transfer", source and destination address is missed. Therefore, the data can be spend to wrong address or can get corrupted due tophysical hardware. Therefore we need to create packet to send data.

For reference or to study more about TCP/IP or UDP, study the book: Data Communication and networking by Forouzan.

Requirement:
python

modules
1. socket(built-in module)
2. Json (built-in module)

Note: the same boiler plate upgardes as we progress from one part to another no new boiler plate is introduced unless stated.