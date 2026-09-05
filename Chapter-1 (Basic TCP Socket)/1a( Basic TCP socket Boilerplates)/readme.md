Chapter-1a

Application- Setup a basic Communication system (part-1).

Objective:
1.To setup a basic Communication system.
2.Create a boiler plate for server and client

Theory:
UDP and TCP are the 2 methods by which any application generally sends data to other application. The application can be both on clients device and also in other device or  to a server. Genrally, the communication can be of 2: unreliable and reliable.

UDP is generally used for unreliable data. You send it and dont care if the other side received it or not. 

TCP is generally used for reliable data. You send it to the destination and wait for acknowledgement from the destination. If acknowledgement is recieved then data is successfully transfered else we wait for a brief amount of time and resend data.

Here the code has additional comments under  each program as to why needed.

For reference or to study more about TCP/IP or UDP, study the book: Data Communication and networking by Forouzan.

Requirement:
python

modules
1. socket(built-in module)

Note: the same boiler plate upgardes as we progress from one part to another no new boiler plate is introduced unless stated.