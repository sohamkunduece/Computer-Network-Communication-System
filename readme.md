# Computer Network Communication System
(Currently ongoing so many readme and other parts are still mising which will be added i due course as we move.)
## Overview

This repository documents my learning journey in Computer Networks through the development of a TCP-based communication system using Python.

The project was not created as a production-ready chat application. Instead, it was built to understand how real-world applications communicate over networks, how messages are transmitted between devices, and how networking concepts taught in textbooks are implemented in practice.

For a basic case, I planned  to go through the evolution on how a message can be transmitted, why various parts is used for contex and what issue is being tackled in each case 

---

## Why This Project?

During my study of Computer Networks, I realized that many concepts such as TCP, sockets, packet transmission, threading, and authentication become much clearer when implemented rather than simply studied.

This project was developed to answer questions such as:

- How do two computers communicate over a network?
- How do messaging applications exchange data?
- How is information formatted and transmitted?
- How do embedded systems communicate with remote devices?
- How do network protocols ensure reliable communication?

By implementing these concepts from scratch, I aimed to bridge the gap between theoretical networking concepts and practical software implementation.

---


## Objectives

The primary objectives of this project are:

- Learn the practical implementation of TCP/IP communication.
- Understand how real-world applications exchange information over networks.
- Explore the internal workflow of client-server communication.
- Study how embedded systems and software applications communicate using networking protocols.
- Build networking concepts incrementally, starting from basic communication and progressing toward secure communication.
- Create a structured learning resource for students beginning their journey in Computer Networks.

---

## Project Structure

The project is divided in cahpters and appendixes. the chapters erve the core story and appendix serves a branch of evolution that is needed.(recap doen till nopw)

chapter 1- how is TCP connection exists in python and why is data send via packets?
chapter 2- why is channel representation needed, what problems come and how does  such things effect teh intregity and security of the system?
chapter 3- why athencation is needed and how does it fixes it with a basic key?
chapter 4- How does hash solve authentication?
chapter 5- How does hmac replaces hashto give a better intregity?

## Technologies Used

- Python
- TCP/IP
- Socket Programming
- Multithreading
- JSON
- Logging

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

- TCP socket programming
- Client-server architecture
- Data transmission over networks
- Concurrent communication using threads
- Authentication mechanisms
- Modular software design
- Practical implementation of networking concepts

---

## Future Scope

The project will continue to evolve with additional networking and security features, including:

- AES Encryption
- RSA Key Exchange
- Secure Session Management
- CRC/Error Detection
- Packet Sequencing
- Acknowledgement & Retransmission
- File Transfer
- Graphical User Interface (GUI)
-and more

It is to be noted that th project act as backbone struture of application. consideing anapplication has 2 parts, a visual operation and a background operation. netwrok is part of background operation

---

## Note

This repository is intended as an educational project for learning Computer Networks. Each folder represents a stage in the development process and demonstrates the gradual implementation of networking concepts rather than a single finished application.