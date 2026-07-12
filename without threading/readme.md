# Stage 1 – Basic Client-Server Communication

## Overview

This is the first stage of the project, focusing on the fundamental architecture of TCP-based client-server communication.

A server listens for incoming connections, while a client establishes a connection and exchanges messages with the server. The communication follows a simple request-response model, making it easier to understand how two applications communicate over a network.

---

## Objective

The objective of this stage is to understand the basic architecture of client-server communication and how data is exchanged using TCP sockets.

This implementation serves as the foundation for the later stages of the project.

---

## Features

- TCP socket communication
- Single client and single server
- Bidirectional message exchange
- Connection establishment and termination
- Simple request-response communication

---

## Limitation

Communication is **sequential**.

After sending a message, one side must wait for the other side to respond before sending another message. As a result, both users cannot communicate simultaneously, making the interaction less natural compared to real-world messaging applications.

---

## Learning Outcomes

After completing this stage, I understood:

- How a server listens for incoming connections.
- How a client establishes a TCP connection.
- How messages are transmitted between two applications.
- The workflow of basic request-response communication.
- Why concurrent communication is necessary in real-world network applications.

---

## Next Stage

The next stage introduces **multithreading**, allowing both client and server to send and receive messages simultaneously.