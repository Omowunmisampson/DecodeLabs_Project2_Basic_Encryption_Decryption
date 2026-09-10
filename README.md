# DecodeLabs_Project2_Basic_Encryption_Decryption
Basic encryption and decryption using a Caesar Cipher in Python.
# Basic Encryption and Decryption - Caesar Cipher

## Project Overview

This project was completed as part of my Cybersecurity Internship with DecodeLabs.

I built a simple Caesar Cipher program using Python to demonstrate how text can be encrypted and decrypted using a shift key.

## How It Works

The program takes a message and moves each letter forward by a specific number of positions in the alphabet.

For example, with a shift of 3:

HELLO → KHOOR

The same shift key is then used to decrypt the message and return it to the original text.

## What I Used

- Python
- ord()
- chr()
- Modulo operator (% 26)
- Shift key
- Encryption and decryption functions

## Features

The program:

- Encrypts uppercase and lowercase letters
- Keeps spaces and punctuation unchanged
- Uses the same key for encryption and decryption
- Decrypts the encrypted message back to the original message
- Includes validation to confirm that the process works correctly

## Testing

I tested the program with different messages, shift keys, spaces, lowercase letters and punctuation.

Example:

Original message:
DecodeLabs Cybersecurity!

Shift key:
13

The encrypted message was successfully decrypted back to:

DecodeLabs Cybersecurity!

Validation result:

PASS

## Security Note

The Caesar Cipher is useful for learning the basic idea of encryption, but it is not secure enough for protecting real-world sensitive information.

It has a very small number of possible shift keys and its letter patterns can still be identified.

## Learning Outcome

This project helped me practise basic encryption and decryption concepts in Python and understand how a simple substitution cipher works.
