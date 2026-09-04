# Stage 2 – Multi-threaded Communication

## Overview

This stage extends the basic client-server architecture by introducing concurrent communication using Python threads. It also introduces a communication channel to simulate how data travels between two endpoints and how messages can be observed or modified during transmission.

---

## Objective

The objectives of this stage are:

- Understand why multithreading is essential in network applications.
- Learn how communication can occur simultaneously rather than sequentially.
- Introduce a communication channel that represents the path between two communicating systems.
- Simulate passive and active interception to understand common network security threats.

---

## Why Multithreading?

In the previous implementation, communication followed a request-response model where one side had to wait for the other before sending another message.

By introducing separate threads for sending and receiving, both operations can execute independently. This allows both users to communicate simultaneously, similar to real-world messaging applications.

---

## Communication Channel

Instead of sending messages directly between the client and server, this stage introduces a communication channel.

The channel represents the path that data follows through a network. In real-world communication, data rarely travels directly between two devices—it passes through routers, switches, gateways, and other networking equipment before reaching its destination.

Using a separate channel also provides a controlled environment to observe and study how data moves through a network.

---

## Simulated Communication Modes

To better understand network communication and security, three communication scenarios are implemented:

### Normal Communication
Messages travel through the communication channel without interference.

### Passive Interception
An observer (Eve) monitors and records transmitted packets without modifying them. This demonstrates how information can be captured during transmission.

### Active Interception
The observer intercepts packets and modifies their contents before forwarding them to the receiver. This demonstrates how data integrity can be compromised during communication.

---

## Learning Outcomes

After completing this stage, I understood:

- Why concurrent execution is required for modern communication systems.
- How threads improve responsiveness in network applications.
- The role of communication channels in representing real-world data transmission.
- The difference between passive packet observation and active packet modification.
- Basic concepts behind network security and interception attacks.

---

## Next Stage

The next stage introduces **user authentication**, ensuring that only authorized users can establish communication before messages are exchanged.