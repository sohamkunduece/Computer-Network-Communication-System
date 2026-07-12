# Stage 3 – User Authentication

## Overview

This stage extends the communication system by introducing user authentication before a client is allowed to communicate with the server.

Instead of accepting every incoming connection, the server verifies the user's credentials before establishing a communication session.

---

## Objective

The objectives of this stage are:

- Understand the role of authentication in network communication.
- Ensure that only authorized users can access the communication system.
- Study how authentication improves communication security.
- Understand the limitations of authentication and why additional security mechanisms are required.

---

## Why Authentication?

In the previous stage, any client capable of connecting to the server could participate in communication.

By introducing authentication, the server verifies the identity of the connecting client before allowing message exchange. This helps prevent unauthorized users from accessing the system.

Authentication is the first step toward building secure communication systems.

---

## How Authentication Improves Security

Authentication helps reduce the impact of certain attacks.

For example, in an **active attack**, an attacker attempting to impersonate a legitimate user must first pass the authentication process. If the credentials cannot be verified, the server rejects the connection.

This ensures that only authenticated users are permitted to communicate.

---

## Limitations

Although authentication verifies **who is communicating**, it does **not** protect **what is being communicated**.

An attacker who can observe network traffic may still capture packets exchanged between authenticated users. This is known as **passive eavesdropping**.

Similarly, if messages are transmitted in plain text after authentication, an attacker who gains access to the communication path may still read or manipulate the transmitted data.

Authentication alone does not provide:

- Confidentiality
- Message Integrity
- Data Encryption

---

## Why Cryptography is Necessary

To secure communication completely, authentication must be combined with cryptographic techniques.

Encryption protects the contents of transmitted messages, ensuring that intercepted packets cannot be understood without the appropriate key.

Future versions of this project will introduce:

- AES Encryption
- RSA Key Exchange
- Secure Session Keys
- Message Integrity Verification

These additions will ensure that communication is both authenticated and protected against eavesdropping and tampering.

---

## Learning Outcomes

After completing this stage, I understood:

- How authentication verifies user identity.
- The difference between authentication and encryption.
- Why authentication alone cannot stop passive eavesdropping.
- Why cryptography is essential for secure communication over untrusted networks.

---

## Next Stage

The next stage will focus on introducing cryptographic techniques to provide confidentiality, integrity, and secure key exchange for network communication.